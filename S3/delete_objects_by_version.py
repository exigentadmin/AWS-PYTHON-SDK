######################################################################################
# Dale Murdock 
# 2025-09-19
#
# This will delete objects by version from an S3 bucket.
######################################################################################

import boto3


client = boto3.client('s3')

def list_obj_by_version(client, bucket):
    response = client.list_object_versions(
    Bucket=bucket
    )
    return response

def create_new_list(dict):
    try:
        # Extract list from dict
        list = dict['Versions']

        # Keys you want to extract
        desired_keys = ["Key", "VersionId"]

        # Create a new list of dictionaries containing only the desired keys
        new_list = [{key: d[key] for key in desired_keys if key in d} for d in list]

        return new_list
    except TypeError as e:
        print(f"Caught an error: {e}")

def delete_objects(client, list, bucket):
    response = client.delete_objects(
    Bucket=bucket,
    Delete={
        'Objects': list
    }
    )

    return response

def main():
    print("Go!")
    try:
        bucket = input("Enter bucket name: ")
        dict = list_obj_by_version(client, bucket)
        new_list = create_new_list(dict)
        status = delete_objects(client, new_list, bucket)
        print(status)
    except TypeError as e:
        print(f"Caught an error: {e}")

if __name__ == "__main__":
    main()