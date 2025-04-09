import boto3
import json

#list all groups using client
connect = boto3.client('connect') #Connect
response = connect.list_queues(
    InstanceId= '59834988-0e27-43c0-8589-cd66ebf3808f',
    QueueTypes= ['STANDARD']
)

#response from aws is a dict
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 ) #convert dict to json

queue_list = response['QueueSummaryList'] #set variable equal to the QueueSummaryList list

# extract queue names from queue_list
queue_names = [item['Name'] for item in queue_list] 
# print queue names
print("\nQueue Names:\n")
print("\n".join(queue_names))

# create new list of chat queues using a filter
chat_queues = [i for i in queue_names if i.endswith("Chat")]
print("\nChat Queues:\n")
print("\n".join(chat_queues))


# extract arn from queue_list
# arn_names = [item['Arn'] for item in queue_list] 
# #print arn names
# print("\nArn Names:\n")
# print("\n".join(arn_names))

# print arn of all queues
# total_queues = 0
# for arn in queue_list:
#     length = len(arn['Arn'])
#     arn_pure = (arn['Arn'])[length - 36:]
#     print(arn_pure)
#     total_queues += 1
#     #print(arn['Arn'])
# print('\nTotal queues ', total_queues)



