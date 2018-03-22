#!/usr/bin/env python
import pika

#connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

#send using credentials: username/password/msg queue host/port/virtual host:
credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost', 5672 ,'/', credentials)

#create connection using cred
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

#declare an exchange:
channel.exchange_declare(exchange='helloexchange', exchange_type='fanout')

#declare queue to use
channel.queue_declare(queue='hello')


# create new message in queue just declared
channel.basic_publish(exchange='helloexchange',
                      routing_key='hello',
                      body='Hello World!')
# say it
print(" [x] Sent 'Hello World!'")
connection.close()
