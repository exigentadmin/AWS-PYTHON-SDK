import boto3
import json
from boto3.dynamodb.conditions import Key

client = boto3.resource('dynamodb')
table = client.Table('ivr_flags')
response = table.query(
    KeyConditionExpression=Key('LOB').eq('Pharmacy')
)

response_json = json.dumps(response, indent = 4)


print(response_json)