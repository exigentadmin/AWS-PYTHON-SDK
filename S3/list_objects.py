import boto3
import json
import pprint
import yaml


bucket = input("Enter bucket name: ")

client = boto3.client('s3')

response = client.list_objects(
    Bucket=bucket
)

#print(yaml.dump(response, default_flow_style=False))

#convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 ) 

print(response_json)