import boto3
import json

client = boto3.client('cognito-idp')

response = client.describe_user_pool(
    UserPoolId='us-east-1_p6oveW877'
)

json_response = json.dumps(
    response,
    indent=4,
    sort_keys=True,
    default=str
)

print(json_response)