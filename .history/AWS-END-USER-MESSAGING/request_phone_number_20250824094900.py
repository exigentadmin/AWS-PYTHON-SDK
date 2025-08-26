import boto3
import json


client = boto3.client('pinpoint-sms-voice-v2')

response = client.request_phone_number(
    IsoCountryCode='string',
    MessageType='TRANSACTIONAL', #The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive.
    NumberCapabilities=[
        'SMS' # Indicates if the phone number will be used for text messages, voice messages, or both.
    ],
    NumberType='SIMULATOR',
    #OptOutListName='string',
    #PoolId='string',
    #RegistrationId='string',
    InternationalSendingEnabled=False,
    DeletionProtectionEnabled=True,
    Tags=[
        {
            'Key': 'Type',
            'Value': 'Demo'
        },
    ],
    # ClientToken='string'
)

