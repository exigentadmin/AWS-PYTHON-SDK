import boto3
import json

client = boto3.client('connect')

def get_instance():
    instance_id = input("Enter Connect instnace id :")
    return instance_id

def list_rp(client, instance_id):
    response = client.list_routing_profiles(
    InstanceId=instance_id,
    # NextToken='string',
    # MaxResults=123
    )
    rp_sum_list = response['RoutingProfileSummaryList']
    


    










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