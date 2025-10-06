######################################################################################
# Dale Murdock 
# 2025-09-21
#
# what am I doing?
######################################################################################
import boto3
import json
import os
from dotenv import find_dotenv, load_dotenv

# load_dotenv() # This loads the variables from the .env file

# instance_id =os.getenv("INSTANCE_IDS")

instance_id ='i-01afda719e4dc97ea'

client = boto3.client('ec2')

response = client.describe_instances(
    InstanceIds=[
        instance_id
    ],

)

# convert dict to json
response_json = json.dumps(
   response,
   indent=4,
   sort_keys=True,
   default=str
)

print(response_json)