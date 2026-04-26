import json
from datetime import datetime
import boto3
import urllib.parse

# Initialize S3, Comprehend and SQS clients
s3 = boto3.client('s3')
comprehend = boto3.client('comprehend')
sqs = boto3.client('sqs')

# Environment variables
HIGH_PRIORITY_QUEUE_URL = "https://sqs.us-east-1.amazonaws.com/321652031960/HighPriorityQueue"
NORMAL_QUEUE_URL = "https://sqs.us-east-1.amazonaws.com/321652031960/NormalQueue"

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(record['s3']['object']['key'])

        # Read file from S3
        response = s3.get_object(Bucket=bucket, Key=key)
        text = response['Body'].read().decode('utf-8')

        # Detect sentiment
        sentiment_response = comprehend.detect_sentiment(
            Text=text,
            LanguageCode='en'
        )

        sentiment = sentiment_response['Sentiment']

        # Sentiment Score
        scores = sentiment_response['SentimentScore']

        # Decide queue
        if sentiment == 'NEGATIVE':
            queue_url = HIGH_PRIORITY_QUEUE_URL
        else:
            queue_url = NORMAL_QUEUE_URL

        # Send message to SQS
        sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps({
                "file": key,
                "text": text,
                "sentiment": sentiment,
                "scores": scores,
                "timestamp": datetime.utcnow().isoformat()
            })
        )

    return {
        'statusCode': 200,
        'body': 'Processed successfully'
    }