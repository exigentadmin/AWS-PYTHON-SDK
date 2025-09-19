import boto3
import json
import pprint
import yaml


bucket = input("Enter bucket name: ")

client = boto3.client('s3')

response = client.list_object_versions(
    Bucket=bucket
)

#convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 )   

print(response_json)
#print(type(response_json))
#print(type(response))
#print(response.keys())

#print(response)

# # Creating a new dict to use in delete objects function
# #######################################################

# # Extract list from dict
# list = response['DeleteMarkers']
# print(list)

# # Keys you want to extract
# desired_keys = ["Key", "VersionId"]

# # Create a new list of dictionaries containing only the desired keys
# new_list = [{key: d[key] for key in desired_keys if key in d} for d in list]

# print(type(new_list))




