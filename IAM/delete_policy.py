import boto3

iam = boto3.client('iam') # IAM low level client object

response = iam.list_policy_versions(
    PolicyArn='arn:aws:iam::195556345987:policy/my-test-bucket-123df-admin-policy'
)

for policy_version in response['Versions']:
    if policy_version['IsDefaultVersion']:
        continue

    response = iam.delete_policy_version(
        PolicyArn='arn:aws:iam::195556345987:policy/my-test-bucket-123df-admin-policy',
        VersionId=policy_version['VersionId']
    )

response = iam.delete_policy(
    PolicyArn='arn:aws:iam::195556345987:policy/my-test-bucket-123df-admin-policy'
)

print(response)

iam_resource = boto3.resource('iam') #resource representing IAM
