import boto3
import json

client = boto3.client('ssm-contacts')

response = client.get_contact_channel(
    ContactChannelId='arn:aws:ssm-contacts:us-east-1:433162890764:contact/dr_reginald_thompson'
)