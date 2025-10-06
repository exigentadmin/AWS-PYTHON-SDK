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
    Filters=[
        {
            'Name': 'free-tier-eligible',
            'Values': [
                'true'
            ]
        },
                {
            'Name': 'image-id',
            'Values': [
                'ami-08982f1c5bf93d976'
            ]
        }

    ]
)
    
# convert dict to json
response_json = json.dumps(
   response,
   indent=4,
   sort_keys=True,
   default=str
)

# print(response_json)

# write response to file
with open('response.json', 'w') as f:
    for i in response_json:
        f.write(i)