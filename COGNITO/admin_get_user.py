import boto3

client = boto3.client('cognito-idp')

response = client.admin_get_user(
    UserPoolId='string',
    Username='string'
)