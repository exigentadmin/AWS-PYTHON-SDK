import boto3

client = boto3.client('cognito-idp')

response = client.admin_add_user_to_group(
    UserPoolId='us-east-1_p6oveW877',
    Username='PingFederate_',
    GroupName='Salesforce'
)

json_response = json.dumps(
    response,
    indent=4,
    sort_keys=True,
    default=str
)

print(json_response)