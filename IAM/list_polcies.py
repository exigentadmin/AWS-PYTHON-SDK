import boto3

iam = boto3.client('iam') # IAM low level client object
response = iam.list_policies(
    Scope = 'AWS'
    #Scope='All'|'AWS'|'Local',
    #OnlyAttached=True|False
)

for user in response['Policies']:
    print("PolicyName: {0}\nCreateDate: {1}\n"
    .format(user['PolicyName'], user['CreateDate']))
