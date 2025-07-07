######################################################################################
# Dale Murdock 
# 2025-03-11
#
# List all routing profiles and arn in the instance
###################################################################################### 
 
import boto3
import json

instance_id = 'daf2d4c6-fd5e-42cd-bd15-41b217b9a48d'

client = boto3.client('connect')

response = client.list_contact_flow_modules(
    InstanceId= instance_id,
    #NextToken='string',
    MaxResults=200,
    ContactFlowModuleState='ACTIVE' #|'ARCHIVED'
)

cfms_list = response['ContactFlowModulesSummaryList']

# print(cfms_list)

module_ids = [item['Id'] for item in cfms_list]
# module_names = [item['Name'] for item in cfms_list]

# print(type(module_ids))

for i in module_ids:
    print(i)

# print(response)

# convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 )

print (response_json)