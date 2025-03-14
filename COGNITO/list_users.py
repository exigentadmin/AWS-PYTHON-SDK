import boto3
import json

client = boto3.client('cognito-idp')

response = client.list_users(
    UserPoolId='us-east-1_p6oveW877',
    # AttributesToGet=[
    #     'email'
    # ]
    Limit=60
    # PaginationToken='string',
    # Filter='string'
)

json_response = json.dumps(
    response,
    indent=4,
    sort_keys=True,
    default=str
)

users = response['Users'] # creates a  list from the dict

#print(users)

for user in users:
    print(user['Username'])

# print(response.keys()) 
# print(response["Users"].keys()) 
# print(type(response))
# print(json_response)