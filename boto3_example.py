# this is the lib that accesses the endpoint

import boto3
from boto3.session import Session

def main():
    # whenever we operate on AWS we have to assume the DSE role and get credentials
    client = boto3.client('sts')
    arn = "arn:aws:iam::833923177614:role/DataScience-Engineering"
    response = client.assume_role(RoleArn=arn, RoleSessionName="boto3")
    response = response['Credentials']

    # Create a lambda session
    lambda_resource=boto3.client('lambda',
        aws_access_key_id=response['AccessKeyId'],
        aws_secret_access_key=response['SecretAccessKey'],
        aws_session_token=response['SessionToken'])
   
    # call your lambda function
    response = lambda_resource.invoke(
        FunctionName="eyang-lambda-dev",
        InvocationType='RequestResponse',
        Payload=b""""""
    )

    #get the output
    output = response['Payload'].read()
    print(output)

if __name__ == '__main__':
    main()