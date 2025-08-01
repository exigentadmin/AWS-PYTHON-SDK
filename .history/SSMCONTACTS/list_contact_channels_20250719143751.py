import boto3
import json

client = boto3.client('ssm-contacts')

response = client.list_contact_channels(
    ContactId='arn:aws:ssm-contacts:us-east-1:433162890764:contact/dr_reginald_thompson'
    # NextToken='string',
    # MaxResults=123
)

# response_json = json.dumps(response, indent = 4)
# print(response_json)
# print(response['Rotations'][0]['ContactIds'])

print(response['ContactChannels'][0]['DeliveryAddress']['SimpleAddress'])