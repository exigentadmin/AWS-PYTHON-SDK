######################################################################################
# Dale Murdock 
# 2025-09-19
#
# List Hours of Opertion
######################################################################################
import boto3
import json
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv() # This loads the variables from the .env file

instance_id =os.getenv("INSTANCE_ID_SANDBOX")

client = boto3.client('connect')

response = client.list_hours_of_operations(InstanceId=instance_id)

# print(response)
# print(response.keys())
# print(response["HoursOfOperationSummaryList"])

# The hours of operation details are in the 'HoursOfOperationSummary' list
for hours_of_operation in response.get('HoursOfOperationSummaryList', []):
    print(f"Name: {hours_of_operation.get('Name')}, ID: {hours_of_operation.get('Id')}")
