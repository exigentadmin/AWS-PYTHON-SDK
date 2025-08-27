import boto3
import json
import os
import logging
from boto3.dynamodb.conditions import Key

# Set logging level to INFO for boto3
logging.getLogger('boto3').setLevel(logging.DEBUG)

# Initialize the boto clients in the global scope
dynamo_client = boto3.resource('dynamodb')
connect_client = boto3.client('connect')

#parse data from event
def parse_data_from_event(event):
        try:
            print("Attributes :", event["Details"]["ContactData"]["Attributes"])
            print("Contact ID :", event["Details"]["ContactData"]["InitialContactId"])
            print("Instance ARN :", event["Details"]["ContactData"]["InstanceARN"])
            print("Line of business :", event["Details"]["ContactData"]["Attributes"]["lineOfBusiness"])
            arn_part = (event["Details"]["ContactData"]["InstanceARN"]).split('/',1)
            instance_id = arn_part[1]
            print("Instance ID :", instance_id)
            contact_id = event["Details"]["ContactData"]["InitialContactId"]
            dynamodb_key = event["Details"]["ContactData"]["Attributes"]["lineOfBusiness"]
        except Exception as e:
            print(e)
            raise e  
        
        return instance_id, contact_id, dynamodb_key


def retreive_messages(key, dynamo_client):
    try:                
        table = dynamo_client.Table(os.environ['table_name'])
        response = table.query(
                KeyConditionExpression=Key(os.environ['partition_key']).eq(key)
            )
        print(f"Messages retreived : {response}")

    except Exception as e:
        print(e)
        raise e  
    
    return response["Items"][0]["prompts"]
      

def update_contact_attributes(instance_id, contact_id, attributes, connect_client):
    try:
        print(f"Start update contact attributes")
        print(instance_id)
        print(contact_id)
        print(attributes)
        response = connect_client.update_contact_attributes(   
            InitialContactId=contact_id,
            InstanceId=instance_id,
            Attributes= attributes
        )
        
    
    except Exception as e:
        logging.error(f"Error updating contact: {e}")
        print(e)
        raise e
    
    print(f"Update success: {response}")
    return response


# Lambda entry
def lambda_handler(event, context):
        # Has lineOfBusiness been sent from the Contact Flow?
        if "lineOfBusiness" in event["Details"]["ContactData"]["Attributes"]:
            try:                   
                # retrive arn and contact id from event
                instance_id, contact_id, dynamodb_key = parse_data_from_event(event)
                #retrive messages from dynamodb
                messages = retreive_messages(dynamodb_key, dynamo_client)
                # send messages to the contact flow as attributes
                update = update_contact_attributes(instance_id, contact_id, messages, connect_client)
            except Exception as e:
                 print(f"Update : {update}")

        else:
             print(f"Line of business not included in contact attributes")

             



