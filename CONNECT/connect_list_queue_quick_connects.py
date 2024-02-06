import boto3
import json

#list all groups using client
connect = boto3.client('connect') #Connect
response = connect.list_queue_quick_connects(
    InstanceId='67faf965-78f3-49d8-a49a-f98a2b061700',
    QueueId='e341658d-2b23-44d9-8685-d9bc79c7e3e7'
)

qcsl_list = response['QuickConnectSummaryList'] #set variable equal to the QueueSummaryList list

#response from aws is a dict
qcsl_list_json = json.dumps(qcsl_list, indent = 4) #convert dict to json

print(qcsl_list_json)