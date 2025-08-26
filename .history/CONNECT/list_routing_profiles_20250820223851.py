import boto3
import json

instance_id = '59208d00-c70f-4b65-b835-4c8e0a41f565'

client = boto3.client('connect')

response = client.list_routing_profiles(
    InstanceId=instance_id,
    # NextToken='string',
    # MaxResults=123
)

rp_sum_list = response['RoutingProfileSummaryList']

for item in rp_sum_list:
    # print("Routing Profile Name :",item["Name"] + "\\t Routing Profile ID :", item["Id"])
    print(f"Routing Profile Name: {item['Name']} \033[24C Routing Profile ID: {item['Id']}")

