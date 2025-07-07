import boto3
import json

instance_id = '0fc85537-a75e-4042-b311-ee8b30e64273'
contact_flow_module_id = 'e77b0271-d391-489d-af3f-03d142160003'


client = boto3.client('connect')

response = client.describe_contact_flow_module(
    InstanceId= instance_id,
    ContactFlowModuleId= contact_flow_module_id)

#print(type(response))

content = response['ContactFlowModule']['Content']

#content = json.loads(response['ContactFlowModule']['Content'])

print(type(content))

print(content)

find = "arn:aws:lambda:us-east-1:438904195518:function:lambda-ssp-au-get-prompts-tes-rcm-phy-2661"

# Using the 'in' operator
if find in content:
    print(f"{find} found in text")


#module_ids = [item['Id'] for item in cfms_list]

# # convert dict to json
# response_json = json.dumps(
#      response,
#      indent=4,
#      sort_keys=True,
#      default=str
#  )

#print (response_json)