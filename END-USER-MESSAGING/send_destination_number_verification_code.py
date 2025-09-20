########################################
import boto3
import json


client = boto3.client('pinpoint-sms-voice-v2')

response = client.send_destination_number_verification_code(
    VerifiedDestinationNumberId='vdn-408259bb2de34e4c87df7eb2f1f31a8e',
    VerificationChannel='TEXT',
    LanguageCode='EN_US',
    OriginationIdentity='phone-8aa5293dcd2c44a5bdc1bc4b77cc28f1', #Using a phone id +14255554596
    ConfigurationSetName='CCIAB-Demo-ConfigSet',
    Context={
        'data': 'custom'
    }
    # DestinationCountryParameters={ #currently only used for Indian phone numbers
    #     'string': 'string'
    # }
)

#convert dict to json
response_json = json.dumps(
    response,
    indent=4,
    sort_keys=True,
    default=str
)

print(response_json)