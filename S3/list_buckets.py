import boto3
import json
import pprint
import yaml

client = boto3.client('s3')
response = client.list_buckets()
print(yaml.dump(response, default_flow_style=False))

