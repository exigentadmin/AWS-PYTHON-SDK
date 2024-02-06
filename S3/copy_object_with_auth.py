import boto3

session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY',
)

s3_client = session.client('s3')

import requests
from requests.auth import aws4auth

def copy_object_with_auth_header(src_bucket, src_key, dest_bucket, dest_key):
    # Create a CanonicalRequest
    canonical_request = create_canonical_request(src_bucket, src_key, dest_bucket, dest_key)

    # Sign the CanonicalRequest
    string_to_sign = create_string_to_sign(canonical_request)
    signature = calculate_signature(string_to_sign)

    # Add the Authorization header
    authorization_header = f'AWS4-HMAC-SHA256 Credential={aws_access_key_id}/{date}/{region}/s3/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-content-sha256;x-amz-date, Signature={signature}'

    # Make the copy_object request with the Authorization header
    copy_source = {
        'Bucket': src_bucket,
        'Key': src_key
    }
    s3_client.copy_object(
        CopySource=copy_source,
        Bucket=dest_bucket,
        Key=dest_key,
        ExtraArgs={
            'Authorization': authorization_header
        }
    )