import boto3
import json

instance_id = '59208d00-c70f-4b65-b835-4c8e0a41f565'

client = boto3.client('connect')

response = client.list_routing_profiles(
    InstanceId=instance_id,
    # NextToken='string',
    # MaxResults=123
)

# convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 )

print (response_json)

rp_sum_list = response_json['RoutingProfileSummaryList']

rp_ids = [item['Id'] for item in rp_sum_list]

for i in rp_ids:
    print(i)