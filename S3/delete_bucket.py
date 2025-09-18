import boto3
import json
import pprint
import yaml

bucket = input("Enter bucket name: ")

client = boto3.client('s3')

response = client.delete_bucket(
    Bucket=bucket
)

print(yaml.dump(response, default_flow_style=False))