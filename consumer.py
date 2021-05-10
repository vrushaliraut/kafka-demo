from kafka import KafkaConsumer
import json

if __name__ == '__main__':
    consumer = KafkaConsumer(
        'registered_user_multiple_partition',
        bootstrap_servers='192.168.0.100:9092',
        auto_offset_reset='earliest',
        group_id='consumer-group-b')

    print("starting a consumer")
    for msg in consumer:
        print("Registered user = {}".format(json.loads(msg.value)))
