import socket
import time
import string
import sys

from confluent_kafka import Consumer, KafkaError, KafkaException

letters = string.ascii_lowercase

conf = {
    'bootstrap.servers': "kafka:9092",
    'client.id': 'client_id',
    'group.id': 'example_consumer',
}

consumer = Consumer(conf)
topic = 'dummy_random'



def main():
    try:
        consumer.subscribe([topic])

        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None: continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    print('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                print(f"Key: {msg.key()} Value:{msg.value()}")
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()
    time.sleep(5)



if __name__ == "__main__":
    print ("Executed when invoked directly")
    main()