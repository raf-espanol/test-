#!/usr/bin/env python
import pika

# this queue is the destination queue
credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
print " connection created"

channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='helloEx', routing_key='', body='Hello World!')
print " [x] Sent 'Hello World!'"
connection.close()

