import boto3
import json

client = boto3.client('lexv2-models')

response = client.list_bots(
    sortBy={
        'attribute': 'BotName',
        'order': 'Ascending'
    },
    filters=[
        {
            'name': 'BotName',
            'values': [
                'medrx',
            ],
            'operator': 'CO'
        },
    ],
    maxResults=60,
    #nextToken='string'
)

# convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 )

print(response_json)

# response = client.list_bots(
#     sortBy={
#         'attribute': 'BotName',
#         'order': 'Ascending'|'Descending'
#     },
#     filters=[
#         {
#             'name': 'BotName'|'BotType',
#             'values': [
#                 'string',
#             ],
#             'operator': 'CO'|'EQ'|'NE' 
#         },
#     ],
#     maxResults=123,
#     nextToken='string'
# )