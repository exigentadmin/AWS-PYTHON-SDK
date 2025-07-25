import boto3
import json

list = ["65efa94c-73f0-4774-b01f-bae4bee96ff4",
"57c3d0c6-864b-405c-9c5e-ada2efc71b7e",
"dae5ab12-1344-4b01-b9ff-3b8a9e4cf7dd",
"5783bc07-1cf2-4341-8dd8-8022ab818281",
"2bb0ae1e-5169-4a32-83fd-42b853aa6e88",
"b3b169a1-4fe9-46fa-8907-f6e137fbfb81",
"c96821c2-e637-4d23-bda1-45b110076612"]

client = boto3.client('connect')

for i in list:
    response = client.describe_contact_flow_module(
    InstanceId= '59834988-0e27-43c0-8589-cd66ebf3808f',
    ContactFlowModuleId= i
    )

    # convert dict to json
    response_json = json.dumps(
        response,
        indent=4,
        sort_keys=True,
        default=str
    ) 
    i += ".json"

    with open(i, 'w') as json_file:
        json_file.write(response_json)