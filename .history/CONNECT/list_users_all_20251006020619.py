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

client = boto3.client('connect')

import boto3

"""
Retrieves all users from an AWS Connect instance using pagination.

:param instance_id: The identifier of the Connect instance.
:param region_name: The AWS region where the instance is located.
:return: A list of all user dictionaries.
"""

users = []
next_token = None

    # Loop until all pages are retrieved
while True:
    # Prepare the request parameters
    params = {
        'InstanceId': instance_id
    }
    if next_token:
        params['NextToken'] = next_token
    
    # Make the API call
    response = client.list_users(**params)
    
    # Extend the users list with the current page's users
    users.extend(response['UserList'])
    
    # Check if there is a next page
    next_token = response.get('NextToken')
    if not next_token:
        break

print(f"Total users retrieved: {len(users)}")
# Print the list of users
for user in users:
    print(user)