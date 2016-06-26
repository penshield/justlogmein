__author__ = 'snouto'

from config import *
from queue import channel , start_listening
from utilities import *
import ast


def callback(ch, method, properties, body):

    if body is not None and len(body) > 0:
        payload = ast.literal_eval(body)
        print ("Received message : %s" % str(payload))
        event = payload['event']
        if event =='send_reset_email':
            pass
        elif event == 'send_confirm_email':
            pass
        elif event == 'add_user':
            pass
        elif event == 'add_site':
            pass

def main():
    print ("Start Listening on Queue : %s" % QUEUE_DEFAULT)
    while True:
        try:
            #start listening on the queue
            start_listening(callback)
        except Exception as s:
            print ("There was an exception : %s" % s.message)
            #here close the connection to the channel
            if channel is not None:
                channel.close()




if __name__ == '__main__':
    main()