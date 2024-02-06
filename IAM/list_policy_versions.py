import boto3

iam = boto3.client('iam') # IAM low level client object
response = iam.list_policy_versions(
    PolicyArn='arn:aws:iam::195556345987:policy/my-test-bucket-123df-admin-policy'
)

for policy_version in response['Versions']:
    print('VersionID: {0}\nIsDefaultVersion: {1}'.format(
    policy_version['VersionId'], policy_version['IsDefaultVersion']
    ))


iam_resource = boto3.resource('iam') #resource representing IAM
policy = iam_resource.Policy('arn:aws:iam::195556345987:policy/my-test-bucket-123df-admin-policy')
policy_version_iterator = policy.versions.all()
for policy_version in policy_version_iterator:
    print(policy_version)
