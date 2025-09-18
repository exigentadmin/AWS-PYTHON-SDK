import json
import boto3
import urllib.parse
from chclib.clients import S3Client
from chclib.helpers import StringBuilders


def lambda_handler(event, context):
    #Get the bucket name from event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    print(bucket_name)
    #Get the source key from event
    source_key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    print("Source key: ", source_key)
    
    if '/UHG' in source_key :
        #Get filename
        filename = StringBuilders.get_key_after_last_delimiter(source_key,"/")

        #Create new filename
        new_filename = StringBuilders.replace_characters(":", "-",filename)
        
        #Create a destination string
        dest_key = source_key.removesuffix(filename)
        dest_key = dest_key.removesuffix('UHG/')
        dest_key = "".join([dest_key, 'RenamedFiles/', new_filename])
        print("Destination key= ", dest_key)
        #Retrieve secret
        #secret = retreive_secret()
        #Convert string to dict
        #secret_dic = json.loads(secret)
        #Assign variable values
        # AWS_ACCESS_KEY = secret_dic['AWS_ACCESS_KEY']
        # AWS_SECRET_ACCESS_KEY = secret_dic['AWS_SECRET_ACCESS_KEY']
        # Create session
        #session = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY,aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name='us-east-1')
        # Initiate client
        # client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
        client = boto3.client('s3')
        raw_obj = client.get_object(Bucket= bucket_name, Key= source_key)
        obj = bytes(raw_obj)
        print('Client =', client)
        try:
            response = client.put_object(Bucket= bucket_name, Key= dest_key)
            print(response)
        except Exception as e:
            print(e)
            print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
            raise e
    else:
        print('Key not equal')

def retreive_secret():
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId='monitoring-automation-ue1-dev-lambda-rename-file-credentials')
    secret = response['SecretString']
    return secret