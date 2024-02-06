import boto3
import json

def lambda_handler(event, context):
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId='exigent/adminkey')
    secret = response['SecretString']
    print(secret)
    # Do something with the secret
    return {
        'statusCode': 200,
        'body': json.dumps('Retrieved secret successfully!')
    }

# Requires the below resource permissions in Secrets Manager
#{
#  "Version" : "2012-10-17",
#  "Statement" : [ {
#    "Effect" : "Allow",
#   "Principal" : {
#      "AWS" : "arn:aws:iam::433162890764:role/ReadSecrets"
#    },
#    "Action" : "secretsmanager:GetSecretValue",
#    "Resource" : "*"
#  } ]
#}