import boto3

#listing all groups using client
iam = boto3.client('iam') # IAM low level client object
response = iam.list_groups()

for group in response['Groups']:
    print("GroupName: {0}\nCreateDate: {1}\n"
    .format(group['GroupName'], group['CreateDate']))
