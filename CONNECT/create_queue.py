######################################################################################
# Dale Murdock 
# 2025-04-09
#
###################################################################################### 
# 
# 

import boto3
import json

instance_id = '59834988-0e27-43c0-8589-cd66ebf3808f'
queue_name = 'ECC-SA_RCM_PatientAccess_Onshore'
tz = 'US/Central'
hoo_id = 'be2b6ab8-9d8a-46a6-aa9d-0c94890c0d47'

client = boto3.client('connect')

response = client.create_queue(
    InstanceId= instance_id,
    Name= queue_name,
    Description= queue_name,
    # OutboundCallerConfig={
    #     'OutboundCallerIdName': 'string',
    #     'OutboundCallerIdNumberId': 'string',
    #     'OutboundFlowId': 'string'
    # },
    # OutboundEmailConfig={
    #     'OutboundEmailAddressId': 'string'
    # },
    HoursOfOperationId= hoo_id,
    # MaxContacts=123,
    # QuickConnectIds=[
    #     'string',
    # ],
    # Tags={
    #     'string': 'string'
    # }
)

#convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 ) 

print(response_json)