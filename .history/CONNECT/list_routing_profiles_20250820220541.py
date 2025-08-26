import boto3
import json

instance_id = '59208d00-c70f-4b65-b835-4c8e0a41f565'

client = boto3.client('connect')

response = client.list_routing_profiles(
    InstanceId=instance_id,
    # NextToken='string',
    # MaxResults=123
)