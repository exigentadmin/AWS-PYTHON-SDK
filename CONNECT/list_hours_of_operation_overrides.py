######################################################################################
# Dale Murdock 
# 2025-09-19
#
# what am I doing?
######################################################################################
import boto3
import json
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv() # This loads the variables from the .env file

instance_id =os.getenv("INSTANCE_ID_DEV-DALE")
hoo_id ="24a783e1-6413-4e74-bd59-66091352f0bb"

client = boto3.client('connect')

response = client.list_hours_of_operation_overrides(
    InstanceId=instance_id,

    HoursOfOperationId=hoo_id
)

# convert dict to json
response_json = json.dumps(
   response,
   indent=4,
   sort_keys=True,
   default=str
)

print(response_json)

# print(response)
# print(response.keys())
# print(response["HoursOfOperationOverrideList"])

# The hours of operation override details are in the 'HoursOfOperationOverrideList' list
# for hours_of_operation in response.get('HoursOfOperationOverrideList', []):
#     print(f"Name: {hours_of_operation.get('Name')}, ID: {hours_of_operation.get('Id')}")

