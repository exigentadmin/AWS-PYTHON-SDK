import boto3

#attaching policy using client
iam = boto3.client('iam') # IAM low level client object
#attaching admin access level policy to group
response = iam.attach_group_policy(
    GroupName='group1',
    PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess'
)
print(response)


#attaching policy using resource
iam = boto3.resource('iam')
group = iam.Group('group2')
#attaching s3 admin access policy to group
response = group.attach_policy(
    PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess'
)
print(response)
