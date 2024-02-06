import boto3

iam = boto3.client('iam') #using low lavel clinet to access IAM

created_user = iam.create_user(
    UserName='second_user',
    Tags=[ # adding tags to identify that user in IAM
        {
            'Key': 'Env',
            'Value': 'Test'
        }
    ]
)
print(created_user)
