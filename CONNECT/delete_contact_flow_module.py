import boto3
import json

client = boto3.client('connect')

response = client.describe_contact_flow_module(
    InstanceId='59834988-0e27-43c0-8589-cd66ebf3808f',
    ContactFlowModuleId='dae5ab12-1344-4b01-b9ff-3b8a9e4cf7dd'
)

# convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 ) 

print(response_json)