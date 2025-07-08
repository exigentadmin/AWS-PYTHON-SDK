import boto3
import urllib.parse


bucket_name = 'exigent-test-lambda-trigger'
source_key = 'Reports/file.txt'
dest_key = 'RenamedReports/file001.txt'

def main():
    try:
        #client = boto3.client('s3')
        get_response = get_s3_object(bucket_name, source_key)
        if(get_response['status'] =='SUCCESS'):
            print('Get SUCCESS')
            try:
                body= get_response['Body']
                put_response = put_s3_object(bucket_name, dest_key, body)
                if(put_response['status'] =='SUCCESS'):
                    print('Put SUCCESS')
                else:
                    print('Put FAIL')
                
            except Exception as e:
                print(e)
                print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.')
                raise e

        else:
            print('OOPS')

    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.')
        raise e
    print('Completed')

def get_s3_object(bucket, key):
    get_status = {}
    s3_client = boto3.client('s3')
    try:
        get_status = s3_client.get_object(Bucket= bucket, Key= key)
        print(get_status.keys())
        print(f'Response: {get_status}')
        if(get_status.get('ResponseMetadata', {}).get('HTTPStatusCode')==200):
            print('get succcess')
            get_status['status'] = 'SUCCESS'        

        else:
            print('get failed')
            get_status['status'] = 'FAILURE'
            get_status['error_msg'] = f'get failed: {get_status}'

        print(f"returning file body")
        return get_status
    except Exception as ex:
        print(f'Error retrieving object from S3 bucket: {ex}') 
        get_status['status'] = 'SERVER_ERROR'
        get_status['error_msg'] = f'Error uploading file into S3 bucket: {ex}'
        return get_status

def put_s3_object(bucket_name: str, key_name: str, stream: bytes):
    body= stream
    put_status = {}
    s3_client = boto3.client('s3')
    try:
        put_status = s3_client.put_object(Bucket= bucket_name, Key= key_name, Body= b'body')
        print(f'Put Response: {put_status}')       

        if(put_status.get('ResponseMetadata', {}).get('HTTPStatusCode')==200):
            print('put succcess')
            put_status['status'] = 'SUCCESS'        

        else:
            print('put failed')
            put_status['status'] = 'FAILURE'
            put_status['error_msg'] = f'put failed: {put_status}'

        print(f"returning file body")
        return put_status
    except Exception as ex:
        print(f'Error putting object from S3 bucket: {ex}') 
        put_status['status'] = StatusCode.SERVER_ERROR
        put_status['error_msg'] = f'Error uploading file into S3 bucket: {ex}'
        return put_status



if __name__ == '__main__':
    main()
'''    try:
        #put object
        put_response = S3Client.put_s3_object(Bucket=bucket_name, Key=dest_key, Body= b'body')
        print(put_response)
        if(put_response.get('HTTPStatusCode')==200):
            print('put succcess')
        else:
            print('put failed')
    except Exception as e:
        print(e)
        print('Error in put object. Make sure they exist and your bucket is in the same region as this function.'.format(dest_key), bucket_name))
        raise e

    else:
        print(f'Key not equal: {source_key}')

def get_s3_object(bucket_name: str, key_name: str):
    get_status = {}
    s3_client = boto3.client('s3')
    try:
        get_status = s3_client.get_object(Bucket= bucket_name, Key= key_name)
        print(f'Response: {get_status}')           
        print(get_status.get('HTTPStatusCode'))

        if(get_status.get('HTTPStatusCode')==200):
            print('get succcess')
            get_status['status'] = 'SUCCESS'        

        else:
            print('get failed')
            get_status['status'] = 'FAILURE'
            get_status['error_msg'] = f'get failed: {get_result}'

        print(f"returning file body")
        return get_status
    except Exception as ex:
        print(f'Error retrieving object from S3 bucket: {ex}') 
        get_status['status'] = StatusCode.SERVER_ERROR
        get_status['error_msg'] = f'Error uploading file into S3 bucket: {ex}'
        return get_status
    
def put_s3_object(bucket_name: str, key_name: str, Body: bytes):
    body= Body
    put_status = {}
    s3_client = boto3.client('s3')
    try:
        response = s3_client.put_object(Bucket= bucket_name, Key= key_name, Body= b'body')
        print(f'Response: {response}')           
        print(response.put('HTTPStatusCode'))

        if(response.put('HTTPStatusCode')==200):
            print('put succcess')
            put_status['status'] = 'SUCCESS'        

        else:
            print('put failed')
            put_status['status'] = 'FAILURE'
            put_status['error_msg'] = f'put failed: {put_status}'

        print(f"returning file body")
        return put_status
    except Exception as ex:
        print(f'Error putting object from S3 bucket: {ex}') 
        put_status['status'] = StatusCode.SERVER_ERROR
        put_status['error_msg'] = f'Error uploading file into S3 bucket: {ex}'
        return put_status
'''