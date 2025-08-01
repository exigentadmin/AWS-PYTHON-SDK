import boto3
import json

client = boto3.client('ssm-contacts')

def list_rotations():
    response = client.list_rotations(
    RotationNamePrefix='PrimaryRotation'
    )
    contact_id = str(response['Rotations'][0]['ContactIds'][0])
    contact_id = contact_id.strip("[']")
    print(contact_id)
    return contact_id
