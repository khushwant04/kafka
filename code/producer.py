from confluent_kafka import Producer
import json
from data import get_registered_user
import time

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = Producer({'bootstrap.servers': '172.17.94.153:9092'})

def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

if __name__ == "__main__":
    while True:
        try:
            registered_user = get_registered_user()
            print(registered_user)
            producer.produce('registered_user', value=json_serializer(registered_user), callback=delivery_report)
            producer.flush()  # Ensure messages are sent
        except Exception as e:
            print(f"Error sending message: {e}")
        time.sleep(2)
