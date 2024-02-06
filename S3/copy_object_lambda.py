import json
import urllib.parse
import boto3

print('Loading function')

client = boto3.client('s3')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    # Get the bucket name from event
    b = event['Records'][0]['s3']['bucket']['name']
    print(event)
    print("Bucket :" + b)
    
    #Get the source key from event
    source_key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    print("Key :" + source_key)
    
    if 'Level1/Level2/UHG/' in source_key :
        #Get the filename from the source_key
        source_list = source_key.rsplit("/")
        list_len = len(source_list)
        filename = source_list[list_len - 1]
        print(filename)
        #create new filename
        new_filename = filename.replace(":", "-")
        try:
            response = client.copy_object(
            Bucket= b,
            CopySource= source_key,
            Key= ("RenamedFiles/"+ new_filename),
            )
            print(response)
        except Exception as e:
            print(e)
            print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
            raise e
    else:
        print('Key not equal')         
