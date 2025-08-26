import boto3
import json

client = boto3.client('connect')

response = client.delete_routing_profile(
    InstanceId='59208d00-c70f-4b65-b835-4c8e0a41f565',
    RoutingProfileId='4b9a52d1-e43b-4db4-93c5-f8f2445a783e'
)
    
# convert dict to json
response_json = json.dumps(
    response,
    indent=4,
    sort_keys=True,
    default=str
)
    
print(response_json)
    


    










client = boto3.client('connect')

response = client.delete_routing_profile(
    InstanceId='string',
    RoutingProfileId='string'
)

# convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 ) 

print(response_json)