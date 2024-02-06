import boto3

#listing all policies attached to group using client
iam = boto3.client('iam') # IAM low level client object
response = iam.list_attached_group_policies(
    GroupName='group1'
    )


for policy in response['AttachedPolicies']:
    print('PolcyName: {0}\nPolicyARN: {1}\n'.format(
    policy['PolicyName'], policy['PolicyArn']
    ))

#listing all policies attached to group using resource
iam = boto3.resource('iam') #resource representing an AWS IAM
group = iam.Group('group2')

policy_iterator = group.attached_policies.all()

for policy in policy_iterator:
    print(policy)
