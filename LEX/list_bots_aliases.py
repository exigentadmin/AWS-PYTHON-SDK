import boto3
import json

client = boto3.client('lexv2-models')

response = client.list_bot_aliases(
    botId='string',
    maxResults=123,
    nextToken='string'
)

# convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 )

print(response_json)