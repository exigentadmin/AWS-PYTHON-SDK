import boto3
import json
import pprint
import yaml

client = boto3.client('s3')

response = client.list_objects(
    Bucket='exigent-tech-test-lambda-trigger-bucket'
)

print(yaml.dump(response, default_flow_style=False))