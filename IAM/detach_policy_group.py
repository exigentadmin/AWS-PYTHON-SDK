import boto3

#detach policy from group using client
iam = boto3.client('iam') # IAM low level client object
response = iam.detach_group_policy(
    GroupName='group1',
    PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess'
)
print(response)

#detach policy from group using resource
iam = boto3.resource('iam') #resource representing an AWS IAM
group = iam.Group('group2')

response = group.detach_policy(
    PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess'
)
print(response)
