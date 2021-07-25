# CETM67-Assignment2

Project consists of:

python function deployed to AWS S3 bucket as zip package using GitHub Actions

AWS SAM 



## linters

flake8 ./assignment_lambda --exclude=env,E501 > static_code_analysis_reports/flake8_output.txt

bandit -r ./assignment_lambda > static_code_analysis_reports/bandit_output.txt

pylint ./assignment_lambda --ignore=env > static_code_analysis_reports/pylint_output.txt

safety check > static_code_analysis_reports/safety_output.txt

## AWS SAM

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html

Deploys AWS lambda and API Gateway

check version 

```sam --version```

# Step 1 Download sample appliation

```sam init```

choose AWS Quick Start Templates

then choose 1 Zip package this will be uploaded to S3

programing language

then hello world example


cd into sam-app then run 

```sam build```

test locally (requires docker)

```sam local start-api```

it can take a while to run docker 

then hit the end point for http://localhost:port/hello

another way is to directly invoke the lambda function using the following command

```sam local invoke "HelloWorldFunction" -e events/event.json```

Clean up
If you no longer need the AWS resources that you created by running this tutorial, you can remove them by deleting the AWS CloudFormation stack that you deployed.

To delete the AWS CloudFormation stack using the AWS Management Console, follow these steps:

Sign in to the AWS Management Console and open the AWS CloudFormation console at https://console.aws.amazon.com/cloudformation.

In the left navigation pane, choose Stacks.

In the list of stacks, choose sam-app (or the name of the stack that you created).

Choose Delete.

When done, the status of the stack changes to DELETE_COMPLETE.

Alternatively, you can delete the AWS CloudFormation stack by running the following AWS CLI command:

aws cloudformation delete-stack --stack-name sam-app --region region
Verify the deleted stack
For both methods of deleting the AWS CloudFormation stack, you can verify that it was deleted by going to the AWS CloudFormation console. In the left navigation pane, choose Stacks, and then in the dropdown list next to the search box, choose Deleted. You should see your stack's name in the list of deleted stacks.