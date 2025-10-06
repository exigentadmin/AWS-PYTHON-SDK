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

instance_id =os.getenv("INSTANCE_ID_OKTA")
email = "Imma.B.Agent@test.com"

client = boto3.client('connect')

paginator = client.get_paginator('list_users')

response_iterator = paginator.paginate(
    InstanceId=instance_id,
    PaginationConfig={
        'MaxItems': 123,
        'PageSize': 123,
        'StartingToken': 'string'
    }
)

print(type(response_iterator))

# user_list = response_iterator['UserSummaryList'] # Extract the list of users
# for user in user_list:
#     if email == user['Username']:
#         print("Found the user!")
#         print(user['Id'])

# # convert dict to json
# response_json = json.dumps(
#    response,
#    indent=4,
#    sort_keys=True,
#    default=str
# )

# print(response.keys())

# print(response_json)


