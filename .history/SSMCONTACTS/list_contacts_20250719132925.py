import boto3
import json

client = boto3.client('ssm-contacts')

response = client.list_contacts(
    # NextToken='string',
    # MaxResults=123,
    # AliasPrefix='string',
    # Type='PERSONAL'|'ESCALATION'|'ONCALL_SCHEDULE'
)