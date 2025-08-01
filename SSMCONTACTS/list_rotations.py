import boto3
import json

client = boto3.client('ssm-contacts')

response = client.list_rotations(
    RotationNamePrefix='PrimaryRotation'
    # NextToken='string',
    # MaxResults=123
)

print(response)
# print(response['Rotations'][0]['RotationArn'])
print(response['Rotations'][0]['ContactIds'][0])

contact_id = str(response['Rotations'][0]['ContactIds'][0])
contact_id = contact_id.strip("[']")

print(contact_id)