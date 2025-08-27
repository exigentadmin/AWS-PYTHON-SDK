import boto3
import json 

client = boto3.client('connect')

response = client.update_contact_attributes(
    InitialContactId='0822b402-b04e-42e9-90ea-bed0c244159c',
    InstanceId='5f89d8a2-63ee-4d5f-8810-462cba28af11',
    Attributes={
        'oncallNumber': '+18005551212'
    }
)

# convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 )

print (response_json)