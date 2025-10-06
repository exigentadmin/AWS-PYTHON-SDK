######################################################################################
# Dale Murdock 
# 2025-09-21
#
# what am I doing?
######################################################################################
import boto3
import json


client = boto3.client('ec2')

response = client.describe_images(
    # ExecutableUsers=[
    #     'string',
    # ],
    # ImageIds=[
    #     'string',
    # ],
    # Owners=[
    #     'string',
    # ],
    # IncludeDeprecated=True|False,
    # IncludeDisabled=True|False,
    # MaxResults=123,
    # NextToken='string',
    # DryRun=True|False,
    # Filters=[
    #     {
    #         'Name': 'string',
    #         'Values': [
    #             'string',
    #         ]
    #     },
    # ]
)