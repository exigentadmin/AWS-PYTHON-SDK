######################################################################################
# Dale Murdock 
# 2025-09-19
#
# Describe Hours of Operation
######################################################################################
import boto3
import json
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv() # This loads the variables from the .env file

instance_id =os.getenv("INSTANCE_ID_SANDBOX")
hoo_id ="0959d3bc-f5cc-45c2-9248-e7d2b032b8dd"

print(instance_id)

client = boto3.client('connect')

try:
    if instance_id != "" and hoo_id != "":
        response = client.describe_hours_of_operation(
            InstanceId=instance_id,
            HoursOfOperationId=hoo_id
    )

    elif instance_id != "" and hoo_id == "":
        hoo_id=input("Please enter Hours Of Operation Id: ")
        response = client.describe_hours_of_operation(
            InstanceId=instance_id,
            HoursOfOperationId=hoo_id
    )
        
    else:
        hoo_id=input("Please enter Instance Id: ")
        hoo_id=input("Please enter Hours Of Operation Id: ")
        response = client.describe_hours_of_operation(
            InstanceId=instance_id,
            HoursOfOperationId=hoo_id
    )
        
except Exception as e:
    print(e)
    raise e

# convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 ) 

print(response_json)