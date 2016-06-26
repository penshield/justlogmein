__author__ = 'snouto'

import pika
from config import *
from justlogging import logEnabled


channel = None

@logEnabled
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


def start_listening(callback,consumer_tag="justlogmein-listener",queue=QUEUE_DEFAULT):
    global channel
    try:
        credentials = pika.PlainCredentials(username=QUEUE_USERNAME,password=QUEUE_PASSWORD)
        connection = pika.BlockingConnection(parameters=pika.ConnectionParameters(host=QUEUE_HOST,credentials=credentials))
        channel = connection.channel()
        channel.queue_declare(queue=queue)
        channel.basic_consume(consumer_callback=callback,queue=queue,no_ack=False,consumer_tag=consumer_tag)
    except Exception as s:
        raise s
