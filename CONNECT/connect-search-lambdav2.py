import boto3
import json

def get_all_contact_flows(connect_client, instance_id):
    """Retrieves all contact flows for a given Connect instance."""
    paginator = connect_client.get_paginator('list_contact_flows')
    contact_flows = []
    for page in paginator.paginate(InstanceId=instance_id):
        contact_flows.extend(page['ContactFlowSummaryList'])
    return contact_flows

def find_contact_flows_with_lambda(instance_ids, lambda_arn, region_name):
    """Finds contact flows that invoke a specific Lambda function across multiple Connect instances."""
    connect_client = boto3.client('connect', region_name=region_name)
    all_matching_flows = []

    for instance_id in instance_ids:
        print(f"\nChecking instance ID: {instance_id}")
        contact_flows = get_all_contact_flows(connect_client, instance_id)
        num_contact_flows = len(contact_flows)
        print(f'Number of contact flows in this instance: {num_contact_flows}')

        matching_flows = []
        for flow in contact_flows:
            contact_flow_id = flow['Id']
            try:
                contact_flow = connect_client.describe_contact_flow(
                    InstanceId=instance_id,
                    ContactFlowId=contact_flow_id
                )
                content = json.loads(contact_flow['ContactFlow']['Content'])
                for module in content['Actions']:
                    if 'Type' in module and module['Type'] == 'InvokeLambdaFunction':
                        if 'Parameters' in module and 'LambdaFunctionARN' in module['Parameters']:
                            function_arn = module['Parameters']['LambdaFunctionARN'].lower()
                            if function_arn == lambda_arn.lower():
                                new_flow = {
                                    'InstanceId': instance_id,
                                    'Name': flow['Name'],
                                    'Id': contact_flow_id
                                }
                                if new_flow not in matching_flows:
                                    matching_flows.append(new_flow)
            except connect_client.exceptions.ResourceNotFoundException:
                print(f"Contact flow {contact_flow_id} not found in instance {instance_id}. It may have been deleted.")
            except Exception as e:
                print(f"Error processing contact flow {contact_flow_id} in instance {instance_id}: {e}")

        if matching_flows:
            print(f"Found the following contact flows invoking Lambda {lambda_arn} in instance {instance_id}:")
            for flow in matching_flows:
                print(f"  Name: {flow['Name']}, ID: {flow['Id']}")
            all_matching_flows.extend(matching_flows)
        else:
            print(f"No contact flows found invoking the Lambda function {lambda_arn} in instance {instance_id}.")

    return all_matching_flows

def get_all_connect_instances(region_name):
    """Retrieves all Connect instance IDs in a given region."""
    connect_client = boto3.client('connect', region_name=region_name)
    instances = []
    next_token = None
    while True:
        kwargs = {}
        if next_token:
            kwargs['NextToken'] = next_token
        response = connect_client.list_instances(**kwargs)
        instances.extend(response['InstanceSummaryList'])
        next_token = response.get('NextToken')
        if not next_token:
            break
    return [instance['Id'] for instance in instances]

if __name__ == "__main__":
    region_name = input("Enter the AWS region (e.g., us-east-1): ")
    if not region_name:
        print("Region cannot be empty.")
        exit(1)

    lambda_arn = input("Enter the Lambda function ARN: ")
    if not lambda_arn:
        print("Lambda ARN cannot be empty.")
        exit(1)

    instance_selection = input("Check all Connect instances? (yes/no): ").lower()
    if instance_selection == 'yes':
        connect_instance_ids = get_all_connect_instances(region_name)
        if not connect_instance_ids:
            print(f"No Connect instances found in region {region_name}.")
            exit(1)
    elif instance_selection == 'no':
        connect_instance_id = input("Enter the Connect instance ID: ")
        if not connect_instance_id:
            print("Connect Instance ID cannot be empty.")
            exit(1)
        connect_instance_ids = [connect_instance_id]
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        exit(1)

    result = find_contact_flows_with_lambda(connect_instance_ids, lambda_arn, region_name)

    if not result: #Check if no flows were found across all instances
        print(f"\nNo contact flows found invoking the Lambda function {lambda_arn} in any of the specified instances.")