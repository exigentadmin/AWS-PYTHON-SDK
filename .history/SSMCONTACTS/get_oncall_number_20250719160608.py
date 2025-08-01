import boto3
import json

client = boto3.client('ssm-contacts')
rotation_name = 'PrimaryRotation'
initialContactId='64a6aa68-3c7b-4447-abf4-0a9b2e581246',
instanceId='9b41f618-5f0c-4966-aac9-0a76bef0572e', #known variable that comes from the call flow when sent to the lambda

def get_contact_id(rotation_name):
    response = client.list_rotations(
    RotationNamePrefix= rotation_name
    )
    contact_id = str(response['Rotations'][0]['ContactIds'][0])
    contact_id = contact_id.strip("[']")
    print(contact_id)
    return contact_id

def get_oncall_number(contact_id):
    response = client.list_contact_channels(
    ContactId= contact_id
    )
    print(response['ContactChannels'][0]['DeliveryAddress']['SimpleAddress'])
    oncall_number = str(response['ContactChannels'][0]['DeliveryAddress']['SimpleAddress'])
    return oncall_number

def update_contact_attributes(oncall_number, contact_id, instance_id):
    client = boto3.client('connect')
    response = client.update_contact_attributes(
    InitialContactId= contact_id,
    InstanceId= instance_id,
    Attributes={
        'oncallNumber': oncall_number
    }
)


  
try:
    rotation_name= input("Enter Rotation Name :")
    contact_id= get_contact_id(rotation_name)
    oncall_number= get_oncall_number(contact_id)
    update_contact_attributes(oncall_number, initialContactId, instanceId)
except:
    pass


