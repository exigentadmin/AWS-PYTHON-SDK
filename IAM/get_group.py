import boto3

#get specific group using client
iam = boto3.client('iam') # IAM low level client object
response = iam.get_group(
GroupName='group1'
)

print(response['Group']['GroupName'])

#list all users in that group
for user in response['Users']:
    print("UserName: {0}\nCreateDate: {1}\n"
    .format(user['UserName'], user['CreateDate']))
