######################################################################################
# Dale Murdock 
# 2025-03-11
#
# describe queue
###################################################################################### 

import boto3
import json

i_id='67faf965-78f3-49d8-a49a-f98a2b061700'
q_id='d2b13316-2a9c-4472-8b8c-9f5849dee51d'

client = boto3.client('connect')

response = client.describe_queue(
    InstanceId=i_id,
    QueueId=q_id
)

# convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 )

print (response_json)