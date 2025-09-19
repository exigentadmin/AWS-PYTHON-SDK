######################################################################################
# Dale Murdock 
# 2025-09-18
#
# Describe View
######################################################################################

import boto3
import json
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv() # This loads the variables from the .env file

instance_id =os.getenv("INSTANCE_ID_DEV")

view_id = "80971164-5786-4b23-a0cd-d9569d3f8c8f"

client = boto3.client('connect')

if instance_id != "" and view_id != "":
    response = client.describe_view(
    InstanceId=instance_id,
    ViewId=view_id
    )

elif instance_id != "" and view_id == "":
    ViewId = input("Please enter ViewId: ")
    response = client.describe_view(
    InstanceId=instance_id,
    ViewId=view_id
    )

else:
    InstanceId = input("Please enter InstanceId: ")
    ViewId = input("Please enter ViewId: ")
    response = client.describe_view(
    InstanceId=instance_id,
    ViewId=view_id
    )


    
# convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 ) 

print(response_json)