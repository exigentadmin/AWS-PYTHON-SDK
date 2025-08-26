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
# response_json = json.dumps(
#      response,
#      indent=4,
#      sort_keys=True,
#      default=str
#  )

# print (response_json)

rp_sum_list = response['RoutingProfileSummaryList']

for item in rp_sum_list:
    # print("Routing Profile Name :",item["Name"] + "\\t Routing Profile ID :", item["Id"])
    print(f"Routing Profile Name: {item['Name']}\t\t Routing Profile ID: {item['Id']}")


# my_list = ['one', 'potato', 'two', 'potato', 'three', 'potato', 'four', 'potato']
columns = 2

# for first, second in zip(my_list[::columns], my_list[1::columns]):
#     print(f'{first: <10}{second}')

for first, second in zip(rp_sum_list[::columns], rp_sum_list[1::columns]):
    print(f'{first['Name']: <10}{second['Id']}')