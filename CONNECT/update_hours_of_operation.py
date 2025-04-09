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

response = client.update_hours_of_operation(
    InstanceId='daf2d4c6-fd5e-42cd-bd15-41b217b9a48d',
    HoursOfOperationId='f21537d8-0318-4eda-bf8d-eabe73defcd2',
    Name='ECC-SA_RCM_PatientAccess_Onshore_HOO',
    Description='ECC-SA_RCM_PatientAccess_Onshore_HOO',
    TimeZone='US/Central',
    Config=[
        {
            Day': 'MONDAY',
            'StartTime': {
                'Hours': 6,
                'Minutes': 30
            },
            'EndTime': {
                'Hours': 19,
                'Minutes': 00
            },
            'Day': 'TUESDAY',
            'StartTime': {
                'Hours': 6,
                'Minutes': 30
            },
            'EndTime': {
                'Hours': 19,
                'Minutes': 00
            },
            'Day': 'WEDNESDAY',
            'StartTime': {
                'Hours': 6,
                'Minutes': 30
            },
            'EndTime': {
                'Hours': 19,
                'Minutes': 00
            },
            'Day': 'THURSDAY',
            'StartTime': {
                'Hours': 6,
                'Minutes': 30
            },
            'EndTime': {
                'Hours': 19,
                'Minutes': 00
            },
            'Day': 'FRIDAY',
            'StartTime': {
                'Hours': 6,
                'Minutes': 30
            },
            'EndTime': {
                'Hours': 19,
                'Minutes': 00
            }
        },
    ]
)