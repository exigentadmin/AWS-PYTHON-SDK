import boto3
import json

client = boto3.client('ssm-contacts')

response = client.list_rotations(
    # RotationNamePrefix='string',
    # NextToken='string',
    # MaxResults=123
)



print(response)