import boto3
import json

print(f"This will print the flow names and arn of the flows containing the text key\n")
instance_id = input(f"Enter Instance ID: ")
key = input(f"Enter text key in flow name: ")

client = boto3.client('connect')

response = client.list_contact_flows(
    InstanceId= instance_id,
    MaxResults=400
)

cfs_list = response['ContactFlowSummaryList']

print(type(cfs_list))

for i in cfs_list:
    if key in i['Name']:
        length = len(i['Arn'])
        arn_pure = (i['Arn'])[length - 36:]
        # print(i['Name'], arn_pure)
        print(f"\"{arn_pure}\",")



# for key, value in cfs_list.items():
#     print(key," ",value)



# print(cfs_list)

# convert dict to json
# cfs_list_json = json.dumps(
#      cfs_list,
#      indent=4,
#      sort_keys=True,
#      default=str
#  ) 

# print(cfs_list_json)


