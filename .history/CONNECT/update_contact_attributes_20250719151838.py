import boto3
import json 

client = boto3.client('connect')

response = client.update_contact_attributes(
    InitialContactId='64a6aa68-3c7b-4447-abf4-0a9b2e581246',
    InstanceId='9b41f618-5f0c-4966-aac9-0a76bef0572e',
    Attributes={
        'oncallNumber': '+18005551212'
    }
)