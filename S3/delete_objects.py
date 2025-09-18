import boto3
import json
import pprint
import yaml
import list_object_versions

bucket = input("Enter bucket name: ")

client = boto3.client('s3')

response = client.delete_objects(
    Bucket=bucket,
    Delete={
        'Objects': [
            {
                'Key': 'string',
                'VersionId': 'string'
            },
        ],
        'Quiet': True|False
    }
)