from kafka import KafkaProducer
import json
from data import get_registerd_user
import time

def json_serrializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=json_serrializer
)

if __name__ == "__main__":
    while 1==1:
        registered_user = get_registerd_user()
        print(registered_user)
        producer.send("quickstart-events", registered_user)
        time.sleep(4)
