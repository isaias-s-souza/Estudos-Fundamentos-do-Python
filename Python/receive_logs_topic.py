#!/usr/bin/env python
import pika, sys, os

def main():
    credentials = pika.PlainCredentials('iofsyswj:iofsyswj', 'cBKkdi42qq0BQc42o6g1MMDBzLNxUd8C')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='jackal.rmq.cloudamqp.com', port=1883, credentials=credentials))
    channel = connection.channel()

    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    binding_keys = sys.argv[1:]
    if not binding_keys:
        sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
        sys.exit(1)

    for binding_key in binding_keys:
        channel.queue_bind(
            exchange='topic_logs', queue=queue_name, routing_key=binding_key)

    print(' [*] Waiting for logs. To exit press CTRL+C')


    def callback(ch, method, properties, body):
        print(" [x] %r:%r" % (method.routing_key, body.decode()))


    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)