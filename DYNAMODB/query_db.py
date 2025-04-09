import boto3
import json

client = boto3.client('dynamodb')

response = client.query(
    TableName='con-aws-ue1-global-dev-appdev-ddb-ivr-config',
    IndexName='string',
    Select='ALL_ATTRIBUTES',
    AttributesToGet=[
        'string',
    ],
    Limit=123,
    ConsistentRead=True|False,
    KeyConditions={
        'string': {
            'AttributeValueList': [
                {
                    'S': 'string',
                    'N': 'string',
                    'B': b'bytes',
                    'SS': [
                        'string',
                    ],
                    'NS': [
                        'string',
                    ],
                    'BS': [
                        b'bytes',
                    ],
                    'M': {
                        'string': {'... recursive ...'}
                    },
                    'L': [
                        {'... recursive ...'},
                    ],
                    'NULL': True|False,
                    'BOOL': True|False
                },
            ],
            'ComparisonOperator': 'EQ'|'NE'|'IN'|'LE'|'LT'|'GE'|'GT'|'BETWEEN'|'NOT_NULL'|'NULL'|'CONTAINS'|'NOT_CONTAINS'|'BEGINS_WITH'
        }
    },
)

response_json = json.dumps(
    response,
    indent=4,
    sort_keys=True,
    default=str
) #convert dict to json


print(response_json)

# response = client.query(
#     TableName='string',
#     IndexName='string',
#     Select='ALL_ATTRIBUTES'|'ALL_PROJECTED_ATTRIBUTES'|'SPECIFIC_ATTRIBUTES'|'COUNT',
#     AttributesToGet=[
#         'string',
#     ],
#     Limit=123,
#     ConsistentRead=True|False,
#     KeyConditions={
#         'string': {
#             'AttributeValueList': [
#                 {
#                     'S': 'string',
#                     'N': 'string',
#                     'B': b'bytes',
#                     'SS': [
#                         'string',
#                     ],
#                     'NS': [
#                         'string',
#                     ],
#                     'BS': [
#                         b'bytes',
#                     ],
#                     'M': {
#                         'string': {'... recursive ...'}
#                     },
#                     'L': [
#                         {'... recursive ...'},
#                     ],
#                     'NULL': True|False,
#                     'BOOL': True|False
#                 },
#             ],
#             'ComparisonOperator': 'EQ'|'NE'|'IN'|'LE'|'LT'|'GE'|'GT'|'BETWEEN'|'NOT_NULL'|'NULL'|'CONTAINS'|'NOT_CONTAINS'|'BEGINS_WITH'
#         }
#     },
#     QueryFilter={
#         'string': {
#             'AttributeValueList': [
#                 {
#                     'S': 'string',
#                     'N': 'string',
#                     'B': b'bytes',
#                     'SS': [
#                         'string',
#                     ],
#                     'NS': [
#                         'string',
#                     ],
#                     'BS': [
#                         b'bytes',
#                     ],
#                     'M': {
#                         'string': {'... recursive ...'}
#                     },
#                     'L': [
#                         {'... recursive ...'},
#                     ],
#                     'NULL': True|False,
#                     'BOOL': True|False
#                 },
#             ],
#             'ComparisonOperator': 'EQ'|'NE'|'IN'|'LE'|'LT'|'GE'|'GT'|'BETWEEN'|'NOT_NULL'|'NULL'|'CONTAINS'|'NOT_CONTAINS'|'BEGINS_WITH'
#         }
#     },
#     ConditionalOperator='AND'|'OR',
#     ScanIndexForward=True|False,
#     ExclusiveStartKey={
#         'string': {
#             'S': 'string',
#             'N': 'string',
#             'B': b'bytes',
#             'SS': [
#                 'string',
#             ],
#             'NS': [
#                 'string',
#             ],
#             'BS': [
#                 b'bytes',
#             ],
#             'M': {
#                 'string': {'... recursive ...'}
#             },
#             'L': [
#                 {'... recursive ...'},
#             ],
#             'NULL': True|False,
#             'BOOL': True|False
#         }
#     },
#     ReturnConsumedCapacity='INDEXES'|'TOTAL'|'NONE',
#     ProjectionExpression='string',
#     FilterExpression='string',
#     KeyConditionExpression='string',
#     ExpressionAttributeNames={
#         'string': 'string'
#     },
#     ExpressionAttributeValues={
#         'string': {
#             'S': 'string',
#             'N': 'string',
#             'B': b'bytes',
#             'SS': [
#                 'string',
#             ],
#             'NS': [
#                 'string',
#             ],
#             'BS': [
#                 b'bytes',
#             ],
#             'M': {
#                 'string': {'... recursive ...'}
#             },
#             'L': [
#                 {'... recursive ...'},
#             ],
#             'NULL': True|False,
#             'BOOL': True|False
#         }
#     }
# )