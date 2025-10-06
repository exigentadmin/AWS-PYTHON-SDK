######################################################################################
# Dale Murdock 
# 2025-10-06
#
# what am I doing?
######################################################################################
import boto3
import json
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv() # This loads the variables from the .env file

api_id =os.getenv("API_ID")
stage_name='verify'
export_type="oas30"

client = boto3.client('apigateway')

response = client.get_export(
    restApiId=api_id,
    stageName=stage_name,
    exportType=export_type,
    # parameters={
    #     'string': 'string'
    # },
    accepts='application/json'
)

print(response['body'].read().decode())

# convert dict to json
response_json = json.dumps(
   response,
   indent=4,
   sort_keys=True,
   default=str
)

print(response_json)