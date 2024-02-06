#The following example copies an object from one bucket to another.
import boto3

client = boto3.client('s3')

b='exigent-test-lambda-trigger'

response = client.copy_object(
    Bucket=b,
    CopySource='/exigent-test-lambda-trigger/Level1/Level2/UHG/New-Text-Document00:00:00.txt',
    Key='RenamedFiles/New-Text-Document-01-00:00:00.txt',
)

print(response)