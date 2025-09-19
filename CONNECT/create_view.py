######################################################################################
# Dale Murdock 
# 2025-09-18
#
# Creatinga  view with .env variable
######################################################################################
import boto3
import json
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv() # This loads the variables from the .env file

instance_id =os.getenv("INSTANCE_ID_DEV-DALE")

client = boto3.client('connect')

response = client.create_view(
    InstanceId=instance_id,
    Status='SAVED', # 'PUBLISHED'|'SAVED'
    Content={
        'Template': '{\"Body\":[{\"Type\":\"Header\",\"_id\":\"Header_1755750690026\",\"Configuration\":{\"Style\":{\"--header-h3-color\":\"#901688\"}},\"Props\":{\"variant\":\"h3\",\"description\":\"\"},\"Content\":[\"Please provide a date\"]},{\"Type\":\"Form\",\"_id\":\"Form_1755750722937\",\"Configuration\":{\"Layout\":{\"Align\":\"center\"},\"Style\":{\"--form-border-color\":\"#901688\"}},\"Props\":{\"HideBorder\":false},\"Content\":[{\"Type\":\"DatePicker\",\"_id\":\"datePicker\",\"Props\":{\"Label\":\"Date\",\"DefaultValue\":\"\",\"HelperText\":\"\",\"Required\":true,\"DateFormat\":\"MM-dd-yyyy\",\"Name\":\"date\"},\"Content\":[]},{\"Type\":\"TemplateStringComponent\",\"_id\":\"TemplateStringComponent_1755750751994\",\"Props\":{\"TemplateString\":\"<hr />\"},\"Content\":[]},{\"Type\":\"SubmitButton\",\"_id\":\"SubmitButton_1755750722937\",\"Configuration\":{\"Style\":{\"--button-border-color--secondary\":\"#901688\"}},\"Props\":{\"Variant\":\"normal\",\"Label\":\"Live Agent\",\"Action\":\"Date Provided\"},\"Content\":[]}]}],\"Head\":{\"Configuration\":{\"Layout\":{\"Columns\":[12],\"Align\":\"center\"},\"Style\":{\"--primary-color-200\":\"#bb61ad\",\"--primary-color-100\":\"#cf8ec5\",\"--primary-color-50\":\"#e2bbdb\",\"--primary-color-400\":\"#9c1a8d\",\"--primary-color-300\":\"#ac3e9d\",\"--primary-color-900\":\"#54036a\",\"--primary-color-600\":\"#7f0f81\",\"--primary-color-500\":\"#901688\",\"--primary-color-800\":\"#54036a\",\"--primary-color-700\":\"#700a79\"}},\"Title\":\"PSA_Calendar_View\"}}',
        'Actions': [
            "Date Provided",
        ]
    },
    Description='string',
    Name='PSA_Calendar_View',
    Tags={
        'Dale': 'Test'
    }
)

# convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 ) 

print(response_json)