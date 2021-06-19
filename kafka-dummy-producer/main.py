import socket
import time
import string
import random

from confluent_kafka import Producer

letters = string.ascii_lowercase

conf = {
    'bootstrap.servers': "kafka:9092",
    'client.id': 'client_id'
}
topic = 'dummy_random'
print(conf)
print(f"topic: {topic}")
producer = Producer(conf)



def main():
    while True:
        str_r10 = ''.join(random.choice(letters) for i in range(10))
        msg = f"value: {str_r10}"
        producer.produce(
            topic,
            key="key",
            value=msg
        )
        producer.flush()
        print('Message Sent')
        time.sleep(0.5)


if __name__ == "__main__":
    print ("Executed when invoked directly")
    main()