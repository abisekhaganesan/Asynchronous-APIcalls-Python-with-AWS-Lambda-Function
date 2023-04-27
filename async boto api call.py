import boto3
import urllib3
import json

def lambda_handler(event, context):
    # Get the URL from the S3 bucket
    s3 = boto3.client('s3')
    bucket_name = 'Bucket_name'
    file_key = 'post_function_url.txt'
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    file_contents = response['Body'].read().decode('utf-8')
    json_data = json.loads(file_contents)
    url = json_data['url']
    # return {
    # 'statusCode': 200,
    # 'body': url
    # }
    
    # Construct the request data
    # header = "user_auth"
    # request_data = {
    #     "data_json": {
    #         "header": header,
    #         "username": event['username'],
    #         "password": event['password']
    #     }
    # }


    header = "user_auth"
    data_json = {
        "header": header,
        "username": event['username'],
        "password": event['password']
    }
    request_data = {
        "data_json": json.dumps(data_json)
    }



    # Make the API call
    http = urllib3.PoolManager()
    headers = {'Content-Type': 'application/json'}
    # response = http.request('POST', url, body=json.dumps(request_data).encode('utf-8'), headers=headers)
    
    # return {
    #     'statusCode': 200,
    #     'body': response
    #     }    json.dumps(request_data).encode('utf-8')
    
    http_response = http.request('POST', url, body=json.dumps(request_data).encode('utf-8'), headers=headers)
    response_body = http_response.data.decode('utf-8')
    
    return {
        'statusCode': 200,
        'body': response_body
        }
    
    
    # # Check the response status code
    # if response.status != 200:
    #     raise ValueError(f'API call failed with status code {response.status}: {response.data.decode("utf-8")}')
    # else:
    #     return "success"
    #     # return response.data.decode('utf-8')
