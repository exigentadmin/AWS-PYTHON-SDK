'''
This will retrieve from DynamoDB the routing profiles from table: con-aws-ue1-global-dev-appdev-ddb-ivr-config, item: ccpAttributes

Enter variables below to find 
'''
rp = 'Basic Routing Profile'
tn = 'con-aws-ue1-global-dev-appdev-ddb-ivr-config'
item = 'ccpAttributes'


import boto3
import json

client = boto3.client('dynamodb')

response = client.get_item(
    TableName= tn,
    Key={'Config':
         {'S': item
        }
    }
)

# Use this to drill down into dict key by key. Last stop M give you a list of the routing profiles
# print(response.keys()) 
# print(response["Item"].keys()) 
# print(response["Item"]["routingProfiles"].keys()) 
# print(response["Item"]["routingProfiles"]["M"].keys()) # At this point the routing profiles are listed

rp_list = list(response["Item"]["routingProfiles"]["M"].keys()) # Convert list of keys into a list

# print(type(rp_list))
# print(rp_list)

# Find and print rp 
if rp in rp_list:
    print(f'{rp} found!')
else:
    print("Element not found.")

# Find index of rp
# try:
#     index = rp_list.index(rp)
#     print(f"Index of Basic Routing Profile: {index}")
# except ValueError:
#     print("Element not found in the list.")

# Print list of all routing prifiles
# print("\nRouting Profile Names in con-aws-ue1-global-dev-appdev-ddb-ivr-config:\n")
# print("\n".join(rp_list))

#qcsl_names = [item['Name'] for item in rp_list] #creates a list of the quick connects assigned to the queue

# Convert dict to json
# response_json = json.dumps(
#     response,
#     indent=4,
#     sort_keys=True,
#     default=str
# ) #convert dict to json