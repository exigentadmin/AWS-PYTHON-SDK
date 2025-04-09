import boto3
import json

client = boto3.client('connect')


response = client.get_effective_hours_of_operations(
    InstanceId='67faf965-78f3-49d8-a49a-f98a2b061700',
    HoursOfOperationId='8661d0d1-1472-45e1-a962-4b62f67aed35',
    FromDate='string',
    ToDate='string'
)

# convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 ) 

print(response_json)