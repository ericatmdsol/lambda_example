## How to deploy an AWS Lambda function

### Prereqs

1. Install okta-keyman and aws cli:  pip install awscli aws-okta-keyman
2. aws_okta_keyman -o mdsol -u your_medidata_id -a 0oaj1kcx7aTjEmXas0x7/272 -r
3. Create a new conda environment to install all necessary packages. In our case our test example only requires flask, but feel free to include other libs that you need **KEEP THE PACKAGES TO A MINIMUM**
4. ```EXPORT VIRTUAL_ENV=/home/eyang/miniconda3/envs/(your conda_env)``` (for linux)
    - For windows: https://docs.oracle.com/en/database/oracle/machine-learning/oml4r/1.5.1/oread/creating-and-modifying-environment-variables-on-windows.html
    - If that doesn't work. I'm sorry you're on your own. **HINT HINT** learning linux isn't a bad thing
5. Install zappa ``` pip install zappa```


### When creating a new project

1. zappa init
2. Modify the zappa_settings.json

```json
{
    "dev": {
        "s3_bucket": "eyang-test-2",  # this is a temporary work space. you can create your own 
        "app_function": "example.app",# it's example because our primary file is example.py
        "lambda_handler": "example.lambda_handler",  #the primary function that is going to be run
        "http_methods": ["GET"],    # are we sending info as a GET or a POST Request
        "manage_roles": false,      # Use an existing role for execution, otherwise new roles are created 
        "role_arn":"arn:aws:iam::833923177614:role/acorn-dse-lambda", # the role that we as DS can use for our lambda
        "profile_name": "okta-orangeds"   #okta keyman generates this and allows us to actually do things on aws
    
    }
}
```
3. zappa deploy

The following error can be ignored

```bash
CloudFormation stack missing, re-deploy to enable updates
ERROR:Could not get API ID.
Traceback (most recent call last):
  File "/home/eyang/miniconda3/envs/lambda/lib/python3.9/site-packages/zappa/core.py", line 2420, in get_api_id
    response = self.cf_client.describe_stack_resource(StackName=lambda_name, LogicalResourceId="Api")
  File "/home/eyang/miniconda3/envs/lambda/lib/python3.9/site-packages/botocore/client.py", line 530, in _api_call
    return self._make_api_call(operation_name, kwargs)
  File "/home/eyang/miniconda3/envs/lambda/lib/python3.9/site-packages/botocore/client.py", line 960, in _make_api_call
    raise error_class(parsed_response, operation_name)
botocore.exceptions.ClientError: An error occurred (ValidationError) when calling the DescribeStackResource operation: Stack 'eyang-lambda-dev' does not exist
Oh no! An error occurred! :(
```

### To invoke

```aws lambda invoke --function-name eyang-lambda-dev response.json --profile okta-orangeds```

This is just to test. If you need to use this operationally, you an use boto3 to wrap this in a python script more generally, or turn this into a actual URL (turning into a url is left as an exercise to the reader, since given the need to pass auth information over I find to be a pain in the ass, and for most of our purposes not really necessary, or it's going to be handled by DSE in the context of an app)

```
```

