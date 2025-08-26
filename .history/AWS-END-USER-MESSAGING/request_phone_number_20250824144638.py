# 
# 
# This code will throw an error because InternationalSendingEnabled is not a valid parameter
# The bot3 documentation has "InternationalSendingEnabled" as a valid parameter but when running the code
# it throws an error.
#
# botocore.exceptions.ParamValidationError: Parameter validation failed:
# Unknown parameter in input: "InternationalSendingEnabled", 
# must be one of: IsoCountryCode, MessageType, NumberCapabilities, 
# NumberType, OptOutListName, PoolId, RegistrationId, DeletionProtectionEnabled, Tags, ClientToken


import boto3
import json


client = boto3.client('pinpoint-sms-voice-v2')

response = client.request_phone_number(
    IsoCountryCode='CA', #The ISO country code for the country or region.
    MessageType='TRANSACTIONAL', #The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive.
    NumberCapabilities=[
        'SMS' # Indicates if the phone number will be used for text messages, voice messages, or both.
    ],
    NumberType='SIMULATOR',
    #OptOutListName='string',
    #PoolId='string',
    #RegistrationId='string',
    #InternationalSendingEnabled=False,
    DeletionProtectionEnabled=True,
    Tags=[
        {
            'Key': 'Type',
            'Value': 'Demo'
        },
    ],
    # ClientToken='string'
)

#convert dict to json
response_json = json.dumps(
    response,
    indent=4,
    sort_keys=True,
    default=str
)

print(response_json)



