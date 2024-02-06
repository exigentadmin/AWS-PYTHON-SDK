import boto3

iam = boto3.client('iam') # IAM low level client object

"""
    We need to make sure group is present in AWS IAM
    As we do not have group named Tester, We will create it first
    IN your case you can skip this step if group is already created in your account
    This is test commit.
"""

create_group_response = iam.create_group(GroupName = 'Tester')


#adding user to Tester group
response = iam.add_user_to_group(
UserName = 'first_user', #Name of user
GroupName = 'Tester'
)

print(response)

iam_resource = boto3.resource('iam') #resource representing IAM
group = iam_resource.Group('Tester') # Name of group

response = group.add_user(
UserName='second_user' #name of user
)

print(response)
