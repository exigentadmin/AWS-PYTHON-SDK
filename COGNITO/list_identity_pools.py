import boto3
import json

client = boto3.client('cognito-identity')

response = client.list_identity_pools(
    MaxResults=60,
    NextToken='string'
)

json_response = json.dumps(
    response,
    indent=4,
    sort_keys=True,
    default=str
)

print(json_response)

