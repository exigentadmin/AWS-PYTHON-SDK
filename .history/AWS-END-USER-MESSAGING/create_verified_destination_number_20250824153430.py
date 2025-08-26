########################################
import boto3
import json


client = boto3.client('pinpoint-sms-voice-v2')

response = client.create_verified_destination_number(
    DestinationPhoneNumber='+15616648941',
    Tags=[
        {
            'Key': 'Type',
            'Value': 'Demo'
        },
    ]
    #ClientToken='string'
)

#convert dict to json
response_json = json.dumps(
    response,
    indent=4,
    sort_keys=True,
    default=str
)

print(response_json)