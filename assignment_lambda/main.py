""" Simple python function for testing out GitHub CI process """
import json


def basic_function():
    """return string"""
    return "hello world"


def read_data(file):
    """ load json file """
    try:
        with open(file) as json_file:
            data = json.load(json_file)

        return data

    except Exception as error:
        return str(error)


def extract_analysis(data):
    """ take json input and perform analysis """

    training_details = {'employee_total': 0}

    course_list = set()

    try:
        for value in data.items():
            training_details['employee_total'] = training_details['employee_total'] + 1
            try:
                course_list.add(value['courses'][0]['CourseName'])
            except KeyError:
                pass

        training_details['courses'] = course_list

        return training_details

    except Exception as error:
        return str(error)


if __name__ == '__main__':
    test_data = read_data('test_data.json')
    extract_analysis(test_data)
