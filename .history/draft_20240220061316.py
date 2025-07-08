import hmac
import hashlib
import base64
from datetime import datetime, timedelta, timezone

def sign(key, msg):
    return hmac.new(key, msg.encode(), hashlib.sha256).digest()

def get_signature_key(key, date_stamp, region_name, service_name):
    k_date = sign(('AWS4' + key).encode(), date_stamp)
    k_region = sign(k_date, region_name)
    k_service = sign(k_region, service_name)
    k_signing = sign(k_service, 'aws4_request')
    return k_signing

def create_auth_header(access_key, secret_key, region_name, service_name, method, path, query_string=None, body=None):
    # Set the current time
    t = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    date_stamp = t[:8]

    # Create the canonical request
    canonical_headers = 'host:' + 'your-api-gateway-domain.com' + '\n'
    signed_headers = 'host'
    if query_string:
        canonical_request = method + '\n' + path + '\n' + query_string + '\n' + canonical_headers + '\n' + hashlib.sha256(body.encode()).hexdigest()
    else:
        canonical_request = method + '\n' + path + '\n' + '\n' + canonical_headers + '\n' + hashlib.sha256(body.encode()).hexdigest()

    # Create the string to sign
    algorithm = 'AWS4-HMAC-SHA256'
    credential_scope = date_stamp + '/' + region_name + '/' + service_name + '/' + 'aws4_request'
    string_to_sign = algorithm + '\n' + t + '\n' + credential_scope + '\n' + hashlib.sha256(canonical_request.encode()).hexdigest()

    # Calculate the signature
    signing_key = get_signature_key(secret_key, date_stamp, region_name, service_name)
    signature = base64.b64encode(sign(signing_key, string_to_sign.encode())).decode()

    # Create the authentication header
    auth_header = algorithm + ' ' + 'Credential=' + access_key + '/' + credential_scope + ', ' + 'SignedHeaders=' + signed_headers + ', ' + 'Signature=' + signature
    return auth_header