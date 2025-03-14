import boto3
import json

#list all groups using client
connect = boto3.client('connect') #Connect
response = connect.list_routing_profiles(
    InstanceId='59834988-0e27-43c0-8589-cd66ebf3808f',
    MaxResults=250
)

rp_list = response['RoutingProfileSummaryList'] #set variable equal to the QueueSummaryList list

total_rp = 0

for arn in rp_list:
    length = len(arn['Arn'])
    arn_pure = (arn['Arn'])[length - 36:]
    print(arn['Name'], arn_pure)
    total_rp += 1
    #print(arn['Arn'])

print('\nTotal queues ', total_rp)
