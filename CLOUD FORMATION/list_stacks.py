import boto3
import json

client = boto3.client('cloudformation')

response = client.list_stacks(
    # # NextToken='string',
    # StackStatusFilter=[
    #     'CREATE_COMPLETE'
    # ]
)

stack_list = response['StackSummaries']

json_response = json.dumps(
    response,
    indent=4,
    sort_keys=True,
    default=str
)

#print(stack_list)

for item in stack_list:
    if 'user-to-user' in item['StackName']:
        print(item['StackName'])
        print(item['StackId'])
    else:
        pass
