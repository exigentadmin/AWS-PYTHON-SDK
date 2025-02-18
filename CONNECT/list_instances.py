import boto3
import json
import pprint
from datetime import datetime



#list all groups using client
connect = boto3.client('connect') #C
response = connect.list_instances()

json_response = json.dumps(response, indent=4, sort_keys=True, default=str) 

###instance_id = response['QuickConnectSummaryList']

###instance_id = dict(sorted(response.Id()))

print(json_response)

''' 
print (type(response))
print(response)
'''


