import boto3
import json

client = boto3.client('connect')

response = client.delete_contact_flow(
    InstanceId='string',
    ContactFlowId='string'
)

# convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 ) 

print(response_json)