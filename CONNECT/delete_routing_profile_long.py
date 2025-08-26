import boto3
import json


def get_instance():
    instance_id = str((input("Enter Connect Instance Id :")).strip())
    return instance_id

def list_rp(client, instance_id):
    try:
        response = client.list_routing_profiles(
            InstanceId=instance_id
        )
    except client.exceptions.ResourceNotFoundException as e:
        print(f"Error: {e}")
        return None
    
    rp_sum_list = response['RoutingProfileSummaryList']

    for item in rp_sum_list:
        print(f"Routing Profile Name: {item['Name']} \033[12C Routing Profile ID: {item['Id']}")

def get_rp():
    rp_id = input("Enter Routing Profile ID you would like deleted :")
    return rp_id

def delete_rp(client, instance_id = str, rp_id = str):
    try:
        response = client.delete_routing_profile(
        InstanceId= instance_id,
        RoutingProfileId= rp_id
        )
    except client.exceptions.ResourceNotFoundException as e:
        print(f"Error: {e}")
        return None
    return response

def main():
    client = boto3.client('connect')
    instance_id = get_instance()
    list_rp(client, instance_id)
    rp_id = get_rp()
    response = delete_rp(client, instance_id, rp_id)
    
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