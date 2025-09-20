######################################################################################
# Dale Murdock 
# 2025-09-19
#
# This will describe the hour of operations overrides
######################################################################################
import boto3
import json
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv() # This loads the variables from the .env file

instance_id =os.getenv("INSTANCE_ID_SANDBOX")
hoo_id ="0959d3bc-f5cc-45c2-9248-e7d2b032b8dd"
hoo_o_id="e6751bb0-2304-4d17-bb99-596baea56050"

client = boto3.client('connect')

response = client.describe_hours_of_operation_override(
    InstanceId=instance_id,
    HoursOfOperationId=hoo_id,
    HoursOfOperationOverrideId=hoo_o_id
)

# convert dict to json
response_json = json.dumps(
   response,
   indent=4,
   sort_keys=True,
   default=str
)

print(response_json)