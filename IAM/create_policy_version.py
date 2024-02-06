import boto3
import json

iam = boto3.client('iam') # IAM low level client object

policyDocumet = {
  "Version":"2012-10-17",
  "Statement":[
    {
      "Sid":"AddPerm",
      "Effect":"Allow",
      "Action":["s3:GetObject"],
      "Resource":["arn:aws:s3:::my-test-bucket-123df/*"]
    }
  ]
}

response = iam.create_policy_version(
    PolicyArn='arn:aws:iam::195556345987:policy/my-test-bucket-123df-admin-policy',
    PolicyDocument=json.dumps(policyDocumet),
    SetAsDefault=True
)

print(response)


#same function using resource object

iam_resource = boto3.resource('iam') #resource representing IAM
policy = iam_resource.Policy('arn:aws:iam::195556345987:policy/my-test-bucket-123df-admin-policy')
policy_version = policy.create_version(
    PolicyDocument=json.dumps(policyDocumet),
    SetAsDefault=True
)
print(response)
