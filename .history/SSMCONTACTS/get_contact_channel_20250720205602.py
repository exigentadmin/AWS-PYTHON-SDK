import boto3
import json

client = boto3.client('ssm-contacts')

response = client.get_contact_channel(
    ContactChannelId='string'
)

response_json = json.dumps(response, indent = 4)

print(response_json)