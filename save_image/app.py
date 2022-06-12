import json
import boto3

def lambda_handler(event, context):

    string = event['body']
    encoded_string = string.encode("utf-8")

    s3 = boto3.client('s3')
    request_data = event['queryStringParameters']
    object_id = request_data['id']
    data_key = "{}.topo.image.txt".format(object_id)
    s3.put_object(Bucket="images.thegnarlytyke.com", Key=data_key, Body=encoded_string)

    return {
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "body": json.dumps(
            {
                "message": "save image call successful"
            }
        )
    }
