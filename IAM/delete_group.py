import boto3

#delete group using client
iam = boto3.client('iam') # IAM low level client object

#make sure group should not have any users
#and all attached policies have been removed
#before we can delete that group

response = iam.remove_user_from_group(
    GroupName='group1',
    UserName='user1_g1'
)

response = iam.remove_user_from_group(
    GroupName='group1',
    UserName='user2_g2'
)

response = iam.delete_group(
    GroupName='group1'
)

print(response)

#delete group using resource
iam = boto3.resource('iam')
group = iam.Group('group2')

#i have already removed users and attached polcies from group2
response = group.delete()
print(response)
