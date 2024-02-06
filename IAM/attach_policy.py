import boto3

iam = boto3.client('iam') # IAM low level client object

response = iam.attach_user_policy(
UserName = 'first_user', #Name of user
PolicyArn = 'arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess' # Policy ARN which you want to asign to user
)

print(response)
