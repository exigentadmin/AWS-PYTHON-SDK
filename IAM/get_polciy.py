import boto3

iam = boto3.client('iam') # IAM low level client object
response = iam.get_policy(
    PolicyArn='arn:aws:iam::195556345987:policy/my-test-bucket-123df-admin-policy'
)

print(response)

response = iam.get_policy_version(
    PolicyArn='arn:aws:iam::195556345987:policy/my-test-bucket-123df-admin-policy',
    VersionId='v2'
)

print(response['PolicyVersion']['Document'])


iam_resource = boto3.resource('iam') #resource representing IAM
policy = iam_resource.Policy('arn:aws:iam::195556345987:policy/my-test-bucket-123df-admin-policy')

"""
following functions can be used with policy resouce to get policy level details
attachment_count
create_date
default_version_id
description
is_attachable
path
permissions_boundary_usage_count
policy_id
policy_name
update_date
"""
