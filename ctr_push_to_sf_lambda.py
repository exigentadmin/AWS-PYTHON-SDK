import json
import os
import boto3
import logging
import datetime
import time
from typing import Dict, List, Any, Tuple
import requests
from botocore.exceptions import ClientError

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize AWS clients
s3_client = boto3.client('s3')
sqs_client = boto3.client('sqs')
secretsmanager_client = boto3.client('secretsmanager')

# Environment variables
SF_CREDENTIALS_SECRET_ARN = os.environ.get('SF_CREDENTIALS_SECRETS_MANAGER_ARN')
SF_HOST = os.environ.get('SF_HOST')
SF_USERNAME = os.environ.get('SF_USERNAME')
S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME', 'commonvoice-dlo-zzzt-commons-xxxx-analytics-prd')
SQS_QUEUE_URL = os.environ.get('SQS_QUEUE_URL', 'https://sqs.region.amazonaws.com/account-id/Commonvoice-dlo-ai-cql-connect-prod-dlr')
SF_CUSTOM_OBJECT_API_NAME = os.environ.get('SF_CUSTOM_OBJECT_API_NAME', 'CTR_Analytics__c')
BATCH_SIZE = int(os.environ.get('BATCH_SIZE', 200))  # Salesforce recommended batch size

def lambda_handler(event, context):
    """
    Main Lambda handler function triggered by EventBridge Scheduler.
    """
    try:
        logger.info(f"Starting CTR data processing at {datetime.datetime.now().isoformat()}")
        
        # Get Salesforce credentials
        sf_credentials = get_salesforce_credentials()
        
        # Authenticate with Salesforce
        access_token, instance_url = authenticate_salesforce(sf_credentials)
        
        # Process SQS messages
        process_sqs_messages(access_token, instance_url)
        
        # Process S3 files
        process_s3_files(access_token, instance_url)
        
        return {
            'statusCode': 200,
            'body': json.dumps('CTR data successfully processed and sent to Salesforce')
        }
    
    except Exception as e:
        logger.error(f"Error in lambda_handler: {str(e)}", exc_info=True)
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error processing CTR data: {str(e)}')
        }

def get_salesforce_credentials() -> Dict[str, str]:
    """
    Retrieve Salesforce credentials from AWS Secrets Manager.
    """
    try:
        secret_response = secretsmanager_client.get_secret_value(
            SecretId=SF_CREDENTIALS_SECRET_ARN
        )
        if 'SecretString' in secret_response:
            secret = json.loads(secret_response['SecretString'])
            return {
                'username': SF_USERNAME,
                'password': secret.get('Password', ''),
                'consumer_key': secret.get('ConsumerKey', ''),
                'consumer_secret': secret.get('ConsumerSecret', ''),
                'access_token': secret.get('AccessToken', '')
            }
        else:
            raise ValueError("Secret does not contain SecretString")
    except ClientError as e:
        logger.error(f"Error retrieving Salesforce credentials: {str(e)}")
        raise

def authenticate_salesforce(credentials: Dict[str, str]) -> Tuple[str, str]:
    """
    Authenticate with Salesforce using OAuth 2.0 password flow.
    Returns the access token and instance URL.
    """
    try:
        # Check if we already have a valid access token
        if credentials.get('access_token'):
            logger.info("Using existing access token from secrets manager")
            return credentials['access_token'], SF_HOST
        
        # If no valid access token, request a new one
        auth_url = f"https://{SF_HOST}/services/oauth2/token"
        payload = {
            'grant_type': 'password',
            'client_id': credentials['consumer_key'],
            'client_secret': credentials['consumer_secret'],
            'username': credentials['username'],
            'password': credentials['password']
        }
        
        response = requests.post(auth_url, data=payload)
        response.raise_for_status()
        
        auth_data = response.json()
        access_token = auth_data['access_token']
        instance_url = auth_data['instance_url']
        
        logger.info("Successfully authenticated with Salesforce")
        return access_token, instance_url
    
    except requests.exceptions.RequestException as e:
        logger.error(f"Error authenticating with Salesforce: {str(e)}")
        raise

def process_sqs_messages(access_token: str, instance_url: str) -> None:
    """
    Retrieve and process messages from SQS queue.
    """
    try:
        # Retrieve messages from SQS queue
        response = sqs_client.receive_message(
            QueueUrl=SQS_QUEUE_URL,
            MaxNumberOfMessages=10,
            WaitTimeSeconds=5,
            VisibilityTimeout=60
        )
        
        messages = response.get('Messages', [])
        if not messages:
            logger.info("No messages found in SQS queue.")
            return
        
        logger.info(f"Retrieved {len(messages)} messages from SQS queue.")
        
        # Process messages in batches
        all_records = []
        receipt_handles = []
        
        for message in messages:
            try:
                body = json.loads(message['Body'])
                all_records.append(body)
                receipt_handles.append(message['ReceiptHandle'])
            except json.JSONDecodeError as e:
                logger.error(f"Error parsing SQS message: {str(e)}")
            
        # Process records in batches
        if all_records:
            process_records_in_batches(all_records, access_token, instance_url)
            
            # Delete processed messages
            for receipt_handle in receipt_handles:
                sqs_client.delete_message(
                    QueueUrl=SQS_QUEUE_URL,
                    ReceiptHandle=receipt_handle
                )
            logger.info(f"Deleted {len(receipt_handles)} messages from SQS queue.")
    
    except Exception as e:
        logger.error(f"Error processing SQS messages: {str(e)}", exc_info=True)
        raise

def process_s3_files(access_token: str, instance_url: str) -> None:
    """
    Process CTR data files from S3 bucket.
    """
    try:
        # List objects in S3 bucket
        response = s3_client.list_objects_v2(
            Bucket=S3_BUCKET_NAME,
            Prefix='ctr-data/'  # Adjust prefix as needed
        )
        
        if 'Contents' not in response:
            logger.info(f"No files found in S3 bucket {S3_BUCKET_NAME} with prefix ctr-data/")
            return
        
        # Process each file
        for item in response['Contents']:
            file_key = item['Key']
            
            # Check if it's a JSON file
            if not file_key.endswith('.json'):
                continue
                
            try:
                logger.info(f"Processing file: {file_key}")
                
                # Get file content
                response = s3_client.get_object(Bucket=S3_BUCKET_NAME, Key=file_key)
                file_content = response['Body'].read().decode('utf-8')
                
                # Parse JSON
                ctr_data = json.loads(file_content)
                
                # Handle both single record and array of records
                records = ctr_data if isinstance(ctr_data, list) else [ctr_data]
                
                # Process records in batches
                process_records_in_batches(records, access_token, instance_url)
                
            except Exception as e:
                logger.error(f"Error processing file {file_key}: {str(e)}", exc_info=True)
                
    except Exception as e:
        logger.error(f"Error processing S3 files: {str(e)}", exc_info=True)
        raise

def process_records_in_batches(records: List[Dict], access_token: str, instance_url: str) -> None:
    """
    Process and send records to Salesforce in batches.
    """
    total_records = len(records)
    logger.info(f"Processing {total_records} records in batches of {BATCH_SIZE}")
    
    for i in range(0, total_records, BATCH_SIZE):
        batch = records[i:i + BATCH_SIZE]
        salesforce_batch = []
        
        for record in batch:
            # Map record fields to Salesforce fields
            salesforce_record = map_to_salesforce_fields(record)
            salesforce_batch.append(salesforce_record)
        
        # Send batch to Salesforce
        if salesforce_batch:
            try:
                send_batch_to_salesforce(salesforce_batch, access_token, instance_url)
                logger.info(f"Sent batch {i//BATCH_SIZE + 1} to Salesforce: {len(salesforce_batch)} records")
            except Exception as e:
                logger.error(f"Error sending batch {i//BATCH_SIZE + 1} to Salesforce: {str(e)}", exc_info=True)

def map_to_salesforce_fields(record: Dict[str, Any]) -> Dict[str, Any]:
    """
    Map CTR data fields to Salesforce custom object fields.
    Adjust this mapping based on your specific field requirements.
    """
    # Map your CTR data fields to Salesforce fields
    # This is a generic example - update this based on your actual field mapping requirements
    
    # Check if the record has an 'Id' field for updating existing records
    sf_record = {}
    
    # Example mapping - replace with your actual field mapping
    if 'id' in record:
        sf_record['Id'] = record['id']
    
    # Map other fields (customize as needed)
    if 'timestamp' in record:
        sf_record['Timestamp__c'] = record['timestamp']
    
    if 'click_count' in record:
        sf_record['Click_Count__c'] = record['click_count']
        
    if 'impression_count' in record:
        sf_record['Impression_Count__c'] = record['impression_count']
        
    if 'ctr_value' in record:
        sf_record['CTR_Value__c'] = record['ctr_value']
        
    if 'campaign_id' in record:
        sf_record['Campaign_ID__c'] = record['campaign_id']
        
    if 'source' in record:
        sf_record['Source__c'] = record['source']
    
    # Add any other field mappings as needed
    
    return sf_record

def send_batch_to_salesforce(records: List[Dict[str, Any]], access_token: str, instance_url: str) -> None:
    """
    Send a batch of records to Salesforce using the Composite API.
    Handles both inserts and updates.
    """
    if not records:
        return
    
    # Separate records into inserts and updates based on presence of Id field
    inserts = [record for record in records if 'Id' not in record]
    updates = [record for record in records if 'Id' in record]
    
    # Process inserts
    if inserts:
        try:
            # Using the Composite API for batch inserts
            url = f"{instance_url}/services/data/v58.0/composite/sobjects"
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
            }
            
            payload = {
                'allOrNone': False,
                'records': [
                    {**record, 'attributes': {'type': SF_CUSTOM_OBJECT_API_NAME}} 
                    for record in inserts
                ]
            }
            
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            
            results = response.json()
            logger.info(f"Successfully inserted {sum(1 for r in results if r.get('success', False))} records")
            
            # Log failed records
            failures = [r for r in results if not r.get('success', False)]
            if failures:
                logger.error(f"Failed to insert {len(failures)} records: {failures}")
                
        except requests.exceptions.RequestException as e:
            logger.error(f"Error inserting records to Salesforce: {str(e)}")
            raise
    
    # Process updates
    if updates:
        try:
            # Using the Composite API for batch updates
            url = f"{instance_url}/services/data/v58.0/composite/sobjects"
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
            }
            
            payload = {
                'allOrNone': False,
                'records': [
                    {**record, 'attributes': {'type': SF_CUSTOM_OBJECT_API_NAME}} 
                    for record in updates
                ]
            }
            
            response = requests.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            
            results = response.json()
            logger.info(f"Successfully updated {sum(1 for r in results if r.get('success', False))} records")
            
            # Log failed records
            failures = [r for r in results if not r.get('success', False)]
            if failures:
                logger.error(f"Failed to update {len(failures)} records: {failures}")
                
        except requests.exceptions.RequestException as e:
            logger.error(f"Error updating records in Salesforce: {str(e)}")
            raise