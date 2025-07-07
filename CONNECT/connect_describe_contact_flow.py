import boto3
import json

instance_id = 'daf2d4c6-fd5e-42cd-bd15-41b217b9a48d'
contact_flow_id = 'd8cc5453-4dce-44d8-b9ea-30a362699075'

client = boto3.client('connect')

response = client.describe_contact_flow(
    InstanceId= instance_id,
    ContactFlowId= contact_flow_id
)

# convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 )

print (response_json)