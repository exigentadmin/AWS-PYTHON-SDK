import boto3
import json

client = boto3.client('connect')

response = client.list_quick_connects(
    InstanceId='59834988-0e27-43c0-8589-cd66ebf3808f',
    # NextToken='string',
    MaxResults=100,
    QuickConnectTypes=[
        'QUEUE'
    ]
)

print(response)

#response from aws is a dict
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 ) #convert dict to json

print(response_json)