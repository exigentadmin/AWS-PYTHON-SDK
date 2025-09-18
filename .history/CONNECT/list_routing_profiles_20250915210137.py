import boto3
import json

instance_id = '94fb6307-2cbf-4ba4-8cc9-d30da38e2a6d'

client = boto3.client('connect')

response = client.list_routing_profiles(
    InstanceId=instance_id,
    # NextToken='string',
    # MaxResults=123
)

rp_sum_list = response['RoutingProfileSummaryList']

for item in rp_sum_list:
    # print("Routing Profile Name :",item["Name"] + "\\t Routing Profile ID :", item["Id"])
    print(f"Routing Profile Name: {item['Name']} \033[12C Routing Profile ID: {item['Id']}")

