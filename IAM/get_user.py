import boto3

iam = boto3.client('iam')

response = iam.get_user(UserName = 'second_user')

print(response)
