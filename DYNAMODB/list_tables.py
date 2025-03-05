import boto3
import json

client = boto3.client('dynamodb')

response = client.list_tables(
    Limit=100
)

response_json = json.dumps(
    response,
    indent=4,
    sort_keys=True,
    default=str
) #convert dict to json


print(response_json)
