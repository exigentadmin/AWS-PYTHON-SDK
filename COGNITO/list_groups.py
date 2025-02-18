import boto3
import json

client = boto3.client('cognito-idp')

response = client.list_groups(
    UserPoolId='string',
    Limit=60,
    NextToken='string'
)

json_response = json.dumps(
    response,
    indent=4,
    sort_keys=True,
    default=str
)

print(json_response)