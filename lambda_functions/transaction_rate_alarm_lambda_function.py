from __future__ import print_function
import boto3
import base64

client = boto3.client('sns')

topic_arn = arn:aws:sns:us-east-1:211080085407:TransactionAlarm

def lambda_handler(event, context):
    try:
        client.publish(TopicArn=topic_arn, Message='Investigate sudden surge in orders', Subject='Order Rate Alarm')
        print('Successfully delivered alarm message')
    except Exception:
        print('Delivery failure')