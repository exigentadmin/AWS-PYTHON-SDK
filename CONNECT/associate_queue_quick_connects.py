import boto3
import json

client = boto3.client('connect')

response = client.associate_queue_quick_connects(
    InstanceId='59834988-0e27-43c0-8589-cd66ebf3808f',
    QueueId='1307a614-24e1-482a-b3ea-8fc15949806e',
    QuickConnectIds=[
        '6d2c7634-bbcf-4963-b610-44612206d1c2','3ec51e86-d5b6-46fb-824e-77ca3a65e825'
    ]
)

print(response)

#response from aws is a dict
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 ) #convert dict to json

print(response_json)

# ECC-NETSOL_MEDNET_MN_Portal_Chat - 6d2c7634-bbcf-4963-b610-44612206d1c2
# ECC_NETSOL_MEDNET_iEDI_ENROLLMENT_Chat - 3ec51e86-d5b6-46fb-824e-77ca3a65e825