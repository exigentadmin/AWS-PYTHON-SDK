import boto3
import json

instance_id = '67faf965-78f3-49d8-a49a-f98a2b061700'

import boto3

client = boto3.client('connect')

paginator = client.get_paginator('list_queues')
queue_list = []

for page in paginator.paginate(InstanceId = instance_id, QueueTypes= ['STANDARD']):
    queue_list.extend(page['QueueSummaryList'])

queue_names = [item['Name'] for item in queue_list] 

print(len(queue_names))

#convert dict to json
response_json = json.dumps(
     queue_list,
     indent=4,
     sort_keys=True,
     default=str
 ) 

#print(response_json)


#print(len(response_json))
#print(queues)