########################################
import boto3
import json


client = boto3.client('pinpoint-sms-voice-v2')

response = client.describe_phone_numbers(
    PhoneNumberIds=[
        'phone-8aa5293dcd2c44a5bdc1bc4b77cc28f1',
    ],
    Filters=[
        {
            'Name': 'status',
            'Values': [
                'Active',
            ]
        },
    ],
    NextToken='string',
    MaxResults=123,
    Owner='SELF'|'SHARED'
)

#convert dict to json
response_json = json.dumps(
    response,
    indent=4,
    sort_keys=True,
    default=str
)

print(response_json)



