import boto3

iam = boto3.client('iam')

"""
    Before deleting user we need to remove it from Group
    Otherwise we will get following error
    An error occurred (DeleteConflict) when calling the DeleteUser operation:
    Cannot delete entity, must remove users from group first.
"""

response = iam.remove_user_from_group(
    GroupName='Tester',
    UserName='second_user'
)

print(response)

response = iam.delete_user(
    UserName='second_user'
)

print(response)


iam = boto3.resource('iam')

"""
    Before deleting user we need to remove
    policies attached to that user
    Otherwise we will get following error

    An error occurred (DeleteConflict) when calling the DeleteUser operation:
    Cannot delete entity, must detach all policies first.
"""

#policy arn which we want to detach from user
policy = iam.Policy('arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess')

response = policy.detach_user(
    UserName='first_user'
)

group = iam.Group('Tester')
response = group.remove_user(
    UserName='first_user'
)


#Now we can delete user
user = iam.User('first_user')

user.delete()
