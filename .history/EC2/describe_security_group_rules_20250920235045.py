######################################################################################
# Dale Murdock 
# 2025-09-20
#
# Describe security group rules
######################################################################################
import boto3
import json

sec_grp_rule_id = [''] # List of strings

client = boto3.client('ec2')

response = client.describe_security_group_rules(
    SecurityGroupRuleIds=sec_grp_rule_id
)

# convert dict to json
response_json = json.dumps(
   response,
   indent=4,
   sort_keys=True,
   default=str
)

print(response_json)

