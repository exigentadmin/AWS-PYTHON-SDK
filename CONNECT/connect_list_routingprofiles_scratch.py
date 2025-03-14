import boto3
import json

#list all groups using client
connect = boto3.client('connect') #Connect
response = connect.list_routing_profiles(
    InstanceId='59834988-0e27-43c0-8589-cd66ebf3808f',
    MaxResults=250
)

#print(type(response))
#print(response.keys())
#print(response["Item].keys()) 
# print(response["Item"]["routingProfiles"].keys()) 
# print(response["Item"]["routingProfiles"]["M"].keys()) # At this point the routing profiles are listed
#response from aws is a dict

response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 )  #convert dict to json

#print(response)
#print(response_json)

rp_list = response['RoutingProfileSummaryList'] #set variable equal to the QueueSummaryList list

# print(type(rp_list))
# print(rp_list)

# rp_list_json = json.dumps(
#      response,
#      indent=4,
#      sort_keys=True,
#      default=str
#  )  #convert dict to json

# print(rp_list_json)

total_rp = 0

for arn in rp_list:
    if "Chat" in arn['Name']:
        length = len(arn['Arn'])
        arn_pure = (arn['Arn'])[length - 36:]
        print(arn['Name'], arn_pure)
        #print(arn_pure)
        total_rp += 1
        #print(arn['Arn'])
    else:
        pass

print('\nTotal Routing Profiles ', total_rp)

# for name in rp_list:
#     print(name['Name'])
#     total_rp += 1

# print('\nTotal Routing Profiles ', total_rp)

# total_queues = 0
#
# for arn in rp_list:
#     length = len(arn['Arn'])
#     arn_pure = (arn['Arn'])[length - 36:]
#     print(arn_pure)
#     total_queues += 1
#     #print(arn['Arn'])
#
# print('\nTotal queues ', total_queues)



