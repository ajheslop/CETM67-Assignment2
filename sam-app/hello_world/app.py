import json
import boto3
# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    try:
        # get AWS resouse
        client = boto3.resource('dynamodb')
        
        # dynamodb table name
        table = client.Table('testTerra')
        
        # dynamodb primary key retrieve one item
        response = table.scan()
        items = response['Items']

        tmp_dict = {}
        for count, value in enumerate(items):
            tmp_dict[count] = value

        data = extract_analysis(tmp_dict)
    
        # Construct http response object
        responseObject = {}
        responseObject['statusCode'] = 200
        responseObject['headers'] = {}
        responseObject['headers']['Content-Type'] = 'application/json'
        responseObject['body'] = json.dumps(data)
        
        # Return the response object
        return responseObject
    
    except Exception as error:
        
        # Construct http response object 
        response = {'error_message' : 'an error occured retrieving training details', 'error_detaials': str(error)}
        responseObject = {}
        responseObject['statusCode'] = 500
        responseObject['headers'] = {}
        responseObject['headers']['Content-Type'] = 'application/json'
        responseObject['body'] = json.dumps(response)
        
        # Return the response object
        return responseObject


def extract_analysis(data):
    """ take json input and perform analysis """

    training_details = {'employee_total': 0}

    course_list = set()

    try:
        for key, value in data.items():
            training_details['employee_total'] = training_details['employee_total'] + 1
            try:
                course_list.add(value['courses'][0]['CourseName'])
            except KeyError:
                pass

        tmp_list = list(course_list)
        training_details['courses'] = tmp_list

        return training_details

    except Exception as error:
        return str(error)