import json
import boto3
import base64
import datetime

BUCKET_NAME = "test.data.thegnarlytyke.com"

def lambda_handler(event, context):

    string = event['body']
    encoded_string = string.encode("utf-8")

    s3 = boto3.client('s3')
    request_data = event['queryStringParameters']
    object_id = request_data['id']

    datetime_stamp = datetime.datetime.now().strftime("%G%m%d.%H%M%S.%f")
    
    split_pos = string.find(',')
    base64_image_data = string[split_pos+1:]
    encoded_data = base64_image_data.encode("utf-8")
    data_key = "images/{}.{}.topo.txt".format(object_id,datetime_stamp)
    s3.put_object(Bucket=BUCKET_NAME, Key=data_key, Body=encoded_data)
    
    binary_image_data = base64.b64decode(base64_image_data)
    filename = "{}.{}.topo.jpg".format(object_id,datetime_stamp)
    data_key = "images/{}".format(filename)
    s3.put_object(Bucket=BUCKET_NAME, Key=data_key, Body=binary_image_data)

    return {
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "body": json.dumps(
            {
                "filename": filename
            }
        )
    }
