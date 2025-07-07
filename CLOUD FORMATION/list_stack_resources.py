import boto3
import json

client = boto3.client('cloudformation')

response = client.list_stack_resources(
    StackName='networkssa-user-to-user-appsync'
)

# json_response = json.dumps(
#     response,
#     indent=4,
#     sort_keys=True,
#     default=str
# )

# print(f'{json_response}')

list_resources = response['StackResourceSummaries']

# print(list_resources)

for item in list_resources:
    print(f"Resource: {item['LogicalResourceId']} ARN: {item['PhysicalResourceId']}\n{item['ResourceType']}\n")