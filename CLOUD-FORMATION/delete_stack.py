import boto3
import json

client = boto3.client('cloudformation')

response = client.delete_stack(
    StackName='string',
    RetainResources=[
        'string',
    ],
    RoleARN='string',
    ClientRequestToken='string',
    DeletionMode='STANDARD'|'FORCE_DELETE_STACK'
)

json_response = json.dumps(
    response,
    indent=4,
    sort_keys=True,
    default=str
)

print(json_response)