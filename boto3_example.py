# this is the lib that accesses the endpoint

import boto3
from boto3.session import Session

def main():
    client = boto3.client('sts')
    arn = "arn:aws:iam::833923177614:role/DataScience-Engineering"
    response = client.assume_role(RoleArn=arn, RoleSessionName="boto3")
    response = response['Credentials']
    lambda_resource=boto3.client('lambda',
        aws_access_key_id=response['AccessKeyId'],
        aws_secret_access_key=response['SecretAccessKey'],
        aws_session_token=response['SessionToken'])
   
    response = lambda_resource.invoke(
        FunctionName="eyang-lambda-dev",
        InvocationType='RequestResponse',
        Payload=b""""""
    )
    output = response['Payload'].read()
    print(output)

if __name__ == '__main__':
    main()