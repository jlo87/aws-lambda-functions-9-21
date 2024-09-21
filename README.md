# aws-lambda-python-s3
Build an AWS Lambda function in Python that uses Boto3 to communicate with Amazon S3

## AWS Lambda:
- Let's you run code without provisioning or managing servers
- Triggers your code in response to events
- Scales automatically
- Provides built-in code monitoring and logging with Amazon CloudWatch

### AWS Lambda use cases:
- Web apps
- Backend
- Data processing
- Chatbots
- Amazon Alexa
- IT automation

## Steps to setup env:
1. Build a virtual environment
- `python3 -m venv ~/.venv`
- `source ~/.venv/bin/activate`

2. Install libraries with the Makefile
- `make install`