######################################################################################
# Dale Murdock 
# 2025-09-20
#
# Describe security group rules
######################################################################################
import boto3
import json
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv() # This loads the variables from the .env file

instance_id =os.getenv("INSTANCE_ID")

client = boto3.client('ec2')

response = client.describe_security_group_rules(
    SecurityGroupRuleIds=[
        'sgr-00089cf229f57e5c9',
        'sgr-0c77f166357be43be'
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

