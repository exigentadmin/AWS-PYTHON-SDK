######################################################################################
# Dale Murdock 
# 2025-09-20
#
# Describe security group rules
######################################################################################
import boto3
import json


launch_template_id = ['lt-0b575978357645e3f'] # List of strings
launch_template_name = [''] # List of strings

client = boto3.client('ec2')

response = client.describe_launch_template_versions(
    # DryRun=True|False,
    LaunchTemplateId=launch_template_id,
    # LaunchTemplateName=launch_template_name,
    Versions=[
        '$Default', '$Latest'
    ],
    # MinVersion='string',
    # MaxVersion='string',
    # NextToken='string',
    # MaxResults=123,
    # Filters=[
    #     {
    #         'Name': 'string',
    #         'Values': [
    #             'string',
    #         ]
    #     },
    # ],
    # ResolveAlias=True|False
)

# convert dict to json
response_json = json.dumps(
   response,
   indent=4,
   sort_keys=True,
   default=str
)

print(response_json)