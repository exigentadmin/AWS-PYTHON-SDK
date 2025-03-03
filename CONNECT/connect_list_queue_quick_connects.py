import boto3
import json

#list all groups using client
connect = boto3.client('connect') #Connect
response = connect.list_queue_quick_connects(
    InstanceId='daf2d4c6-fd5e-42cd-bd15-41b217b9a48d',
    QueueId='9e325054-ad63-420f-b985-329793ff6890'
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