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


st_hrs = 6 # No leading zero
st_mins = 00 #requires to digits
et_hrs = 19
et_mins = 00
instance_id = ''
name_hoo = ''
tz = 'US/Central'

client = boto3.client('connect')

response = client.create_hours_of_operation(
    InstanceId= instance_id,
    Name= name_hoo + "_HOO",
    Description= name_hoo + "_HOO",
    TimeZone= tz,
    Config=[
        {
            'Day': 'MONDAY',
            'StartTime': {
                'Hours': st_hrs,
                'Minutes': st_mins
            },
            'EndTime': {
                'Hours': et_hrs,
                'Minutes': et_mins
            }
        },
        {
            'Day': 'TUESDAY',
            'StartTime': {
                'Hours': st_hrs,
                'Minutes': st_mins
            },
            'EndTime': {
                'Hours': et_hrs,
                'Minutes': et_mins
            }
        },
        {
            'Day': 'WEDNESDAY',
            'StartTime': {
                'Hours': st_hrs,
                'Minutes': st_mins
            },
            'EndTime': {
                'Hours': et_hrs,
                'Minutes': et_mins
            }
        },
        {
            'Day': 'THURSDAY',
            'StartTime': {
                'Hours': st_hrs,
                'Minutes': st_mins
            },
            'EndTime': {
                'Hours': et_hrs,
                'Minutes': et_mins
            }
        },
        {
            'Day': 'FRIDAY',
            'StartTime': {
                'Hours': st_hrs,
                'Minutes': st_mins
            },
            'EndTime': {
                'Hours': et_hrs,
                'Minutes': et_mins
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