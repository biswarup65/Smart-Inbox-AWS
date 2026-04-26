import boto3
import json

# Intialize SQS client
sqs = boto3.client('sqs')

# Environment variables
HIGH_PRIORITY_QUEUE_URL = "https://sqs.us-east-1.amazonaws.com/321652031960/HighPriorityQueue"
NORMAL_QUEUE_URL = "https://sqs.us-east-1.amazonaws.com/321652031960/NormalQueue"

def get_messages(queue_url):
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=5,
        WaitTimeSeconds=1
    )
    
    return response.get('Messages', [])

def lambda_handler(event, context):
    high = get_messages(HIGH_PRIORITY_QUEUE_URL)
    normal = get_messages(NORMAL_QUEUE_URL)

    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Origin": "*"
        },
        'body': json.dumps({
            "highPriority": high,
            "normal": normal
        })
    }


