######################################################################################
# Dale Murdock 
# 2025-09-18
#
# Describe a routing profile
######################################################################################

import boto3
import json

i_id='59834988-0e27-43c0-8589-cd66ebf3808f'
rp_id='8d3a3e45-be95-4314-818d-41139b79dc42'

client = boto3.client('connect')

response = client.describe_routing_profile(
    InstanceId=i_id,
    RoutingProfileId=rp_id
)

# convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 )

print (response_json)

list= [
"13547941-ecc2-4bcf-92a9-f3237420ba5a",
"181acd1b-c3c8-4568-8452-9b373e3b44c5",
"22575ca1-4160-4647-83cd-6cc94166b5f0",
"2315a2a9-380a-4c65-8731-3bdc29de3f68",
"26bc97cf-7a8e-429a-b796-3f9c42b8a313",
"30b3afec-069f-416b-a893-918f9d356c4a",
"341144e5-a27f-4eb6-8507-14a147b456b8",
"3a8b6224-482f-4911-a0c7-d57641e42376",
"3f9932f7-a673-4a33-8cda-0ec9fd87a5fe",
"4160598d-c6f6-4d08-825e-2d8046c026b7",
"42da1118-bdb1-49ae-98b5-af8f673fbcfb",
"4361cc23-4a29-426f-b93b-90dcd360dbf2",
"4b1c0803-7a08-48ba-992c-1c4cc856cf81",
"52d3382c-44c7-4f4a-a287-4add51d97f7a",
"5acf713b-e8c7-4a5c-846a-f7d33602c8a8",
"5dec3797-b865-4ef1-bc74-fb1da73f2182",
"7704fb9e-b834-4b97-8435-d7adf42d0b78",
"7de8ced8-e6ef-4cc4-8243-17c0a1086e6e",
"8d3a3e45-be95-4314-818d-41139b79dc42",
"8ea4e7bb-2b5b-4d12-a52c-7b7cdf4fd178",
"9833d21d-9daa-4764-80dd-85c9559400fa",
"9c71ebe9-4f0d-4a38-a11a-52f4d5747c79",
"aa7d9bfc-0634-4e35-ae60-e6aadd43dcf5",
"af7bf501-96e1-4a73-8d45-9e7c67599fff",
"b1441f67-d6b5-4fab-a301-144bf26f982e",
"b17fb234-542e-416e-a5cf-25353bd7247a",
"bcd9f852-4a92-4ecd-bae3-371d4a771ddd",
"c114bbb7-2d2a-45da-a6c6-a3ce7c40dbbb",
"ca302521-e7fc-4667-b4da-6d23a9d7d94e",
"cdf3053f-d9b4-414c-8dd5-e213889671c9",
"d0f77a57-31ef-47e8-944a-ef7aa66e1cdd",
"d8fd3c61-ee0d-419a-8327-2cc87722b5f0",
"d9b2de0f-0d90-4382-ac8d-492bc6bff210",
"e0b0b2bc-823c-4477-b117-c783b71fd7fc",
"eba2f4d3-8cd2-455b-98e0-6bcf3e6d02b8",
"f68f8aab-e8bf-4cd2-aed7-534c98bb002b",
"fd612bf4-8596-429e-8d7b-9e7ff708e5c6",
"ffc14d27-60c2-4ca9-82f0-b6c9c295f68c"
]

# for i in list:
#     try:
#         client = boto3.client('connect')
#         response = client.describe_routing_profile(
#     InstanceId='string',
#     RoutingProfileId='string'
#     )
#     print(response)    
#     except:
#         pass

