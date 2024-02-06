import boto3
import json

iam = boto3.client('iam') # IAM low level client object

policyDocumet = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ListObjectsInBucket",
            "Effect": "Allow",
            "Action": ["s3:ListBucket"],
            "Resource": ["arn:aws:s3:::my-test-bucket-123df"]
        },
        {
            "Sid": "AllObjectActions",
            "Effect": "Allow",
            "Action": "s3:*Object",
            "Resource": ["arn:aws:s3:::my-test-bucket-123df/*"]
        }
    ]
}

response = iam.create_policy(
    PolicyName='my-test-bucket-123df-admin-policy',
    PolicyDocument=json.dumps(policyDocumet),
    Description='Read and Write policy for my-test-bucket-123df bucket'
)


print(response)
