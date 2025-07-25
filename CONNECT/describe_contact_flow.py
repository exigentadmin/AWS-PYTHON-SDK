import boto3
import json

list = ["9eb09f0a-d078-4410-bce0-7547564b2df8",
"44691d98-defd-4ace-947f-58a76d765b3b",
"a967de80-da9b-43f2-8265-b306ab451f25",
"31f7d031-c3c8-44c3-b344-f702fd2b0da9",
"4f3db1ce-5b79-4b7d-983b-6d893ade61e8",
"c76924a6-f176-4c34-9b72-db480bc056e3",
"89811ba4-df56-4596-8dec-e449ac28e4e4",
"5cb01957-91b7-46c2-b4a1-724ffd1e5518",
"bcb2b9fa-ec58-403e-9ff2-264d5b4d47c4",
"46f4956d-67c7-40f8-8550-d26fe5066329",
"192359ee-fbd2-464b-b48a-f0bc870da604",
"bcba2438-696d-4c9e-85fc-6bc63b31310a",
"800db007-ad9f-4a97-a570-037766a36d8d",
"ed56964e-7624-48d7-b081-650e32b7933e",
"dd20cfc2-1dce-47f6-bc57-dae45bb76b3f",
"cb060b7e-bd89-44ab-b3f8-d005b9b87add",
"044edf8b-7301-4bea-8dde-b3b0e83ab478",
"171ebd03-d6d3-46ba-8705-7809abc89bcb",
"5ca76ed9-00f3-4dde-8044-2d735e5fb759",
"fc32584e-4536-4fc8-bd61-c94816cd96b5",
"2c4dc696-6062-48a7-bb7c-04207c31d0e5",
"957b888e-b2ef-434f-9975-484b7c1d053c",
"23f5af19-40d5-4ec4-8ec5-338a169e8d88",
"9d640eea-277a-4eee-b680-e9f785f3d295",
"95aec06b-325a-47f0-82dc-c26a8590f5e0",
"c9733ef2-d268-4cce-bed9-ff48ea79cdeb",
"baeb76cd-17fc-4ccb-b64a-b47b323f406d"]

client = boto3.client('connect')

for i in list:
    response = client.describe_contact_flow(
    InstanceId= '59834988-0e27-43c0-8589-cd66ebf3808f',
    ContactFlowId= i
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






