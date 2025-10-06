######################################################################################
# Dale Murdock 
# 2025-10-05
#
# what am I doing?
######################################################################################
import boto3
import json
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv() # This loads the variables from the .env file

instance_id =os.getenv("INSTANCE_ID_CCIAB")
security_profile_id = os.getenv("SECURITY_PROFILE_IDS")
routing_profile_id = os.getenv("ROUTING_PROFILE_ID")

client = boto3.client('connect')

response = client.create_user(
    Username='test@user.com',
    IdentityInfo={
        'FirstName': 'Test',
        'LastName': 'User',
    },
    PhoneConfig={
        'PhoneType': 'SOFT_PHONE',
        'AutoAccept': False
    },
    SecurityProfileIds=security_profile_id,
    RoutingProfileId=routing_profile_id,
    InstanceId=instance_id,
    Tags={
        'LOB': 'ExigentTech'
    }
)