import boto3
import json

client = boto3.client('cloudformation')

response = client.describe_stack_resources(
    StackName='networkssa-user-to-user-appsync',
    # LogicalResourceId='string',
    # PhysicalResourceId='string'
)


json_response = json.dumps(
    response,
    indent=4,
    sort_keys=True,
    default=str
)

print(json_response)