######################################################################################
# Dale Murdock 
# 2025-04-09
#
# Scratch to test code for given API
###################################################################################### 
# 
# 

import boto3
import json

client = boto3.client('connect')

response = client.create_hours_of_operation(
    InstanceId='daf2d4c6-fd5e-42cd-bd15-41b217b9a48d',
    Name='ECC-SA_RCM_AssuranceRM_Agreements_Onshore_HOO',
    Description='ECC-SA_RCM_AssuranceRM_Agreements_Onshore_HOO',
    TimeZone='US/Central',
    Config=[
        {
            'Day': 'MONDAY',
            'StartTime': {
                'Hours': 7,
                'Minutes': 30
            },
            'EndTime': {
                'Hours': 17,
                'Minutes': 00
            }
        },
        {
            'Day': 'TUESDAY',
            'StartTime': {
                'Hours': 7,
                'Minutes': 30
            },
            'EndTime': {
                'Hours': 17,
                'Minutes': 00
            }
        },
        {
            'Day': 'WEDNESDAY',
            'StartTime': {
                'Hours': 7,
                'Minutes': 30
            },
            'EndTime': {
                'Hours': 17,
                'Minutes': 00
            }
        },
        {
            'Day': 'THURSDAY',
            'StartTime': {
                'Hours': 7,
                'Minutes': 30
            },
            'EndTime': {
                'Hours': 17,
                'Minutes': 00
            }
        },
        {
            'Day': 'FRIDAY',
            'StartTime': {
                'Hours': 7,
                'Minutes': 30
            },
            'EndTime': {
                'Hours': 17,
                'Minutes': 00
            }        
        },
     ]
    # Tags={
    #     'string': 'string'
    # }
)

#convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 ) 

print(response_json)