######################################################################################
# Dale Murdock 
# 2025-09-20
#
# Describe security group rules
######################################################################################
import boto3
import json


launch_template_id = [''] # List of strings

client = boto3.client('ec2')

response = client.describe_launch_templates(
    # DryRun=True|False,
    # LaunchTemplateIds=launch_template_id,
    LaunchTemplateNames=[
        'sshandhomepage',
    ],
    # Filters=[
    #     {
    #         'Name': 'string',
    #         'Values': [
    #             'string',
    #         ]
    #     },
    # ],
    # NextToken='string',
    # MaxResults=123
)