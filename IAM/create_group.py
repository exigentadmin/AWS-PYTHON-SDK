import boto3

#creating group with client
iam = boto3.client('iam') # IAM low level client object
create_group_response = iam.create_group(GroupName = 'group1')
print(create_group_response)

#createing group with resource
iam = boto3.resource('iam') #resource representing IAM
response = iam.create_group(
    GroupName='group2'
)
print(response)
