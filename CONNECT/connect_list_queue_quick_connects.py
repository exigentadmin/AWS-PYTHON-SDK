import boto3
import json

#list all groups using client
connect = boto3.client('connect') #Connect
response = connect.list_queue_quick_connects(
    InstanceId='67faf965-78f3-49d8-a49a-f98a2b061700',
    QueueId='d2b13316-2a9c-4472-8b8c-9f5849dee51d'
)

qcsl_list = response['QuickConnectSummaryList'] #set variable equal to the QueueSummaryList list
#response from aws is a dict

#print(qcsl_list)

qcsl_names = [item['Name'] for item in qcsl_list] #creates a list of the quick connects assigned to the queue

#print(type(qcsl_names))
print("\n".join(qcsl_names))

# qcsl_list_json = json.dumps(
#     qcsl_list,
#     indent=4,
#     sort_keys=True,
#     default=str
# ) #convert dict to json

# print(qcsl_list_json)