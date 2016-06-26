__author__ = 'snouto'

import pika
from config import *
from controllers.logging import logEnabled


def send_queue_message(message,queue=QUEUE_DEFAULT):
    try:
        credentials = pika.PlainCredentials(username=QUEUE_USERNAME,password=QUEUE_PASSWORD)
        connection = pika.BlockingConnection(parameters=pika.ConnectionParameters(host=QUEUE_HOST,credentials=credentials))
        channel = connection.channel()
        channel.queue_declare(queue=queue)
        channel.basic_publish(exchange=QUEUE_EXCHANGE_NAME,routing_key=queue,body=str(message))
        channel.close()
        connection.close()
        return True
    except Exception as s:
        print s.message
        return False
