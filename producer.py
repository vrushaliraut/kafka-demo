from kafka import KafkaProducer
import json
from data import get_registered_user
import time


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


def get_partition(key, all, available):
    return 0


getProducerwithSinglePartition = KafkaProducer(bootstrap_servers=['192.168.0.100:9092'],
                                               value_serializer=json_serializer)

producer = KafkaProducer(bootstrap_servers=['192.168.0.100:9092'],
                         value_serializer=json_serializer)

producer_with_assigned_partition = KafkaProducer(bootstrap_servers=['192.168.0.100:9092'],
                                                 value_serializer=json_serializer,
                                                 partitioner=get_partition)


def send_message_single_partition():
    producer.send("registered_user", registered_user)
    pass


def send_message_multiple_partition():
    producer.send("registered_user_multiple_partition", registered_user)
    pass


def send_message_perticular_partition():
    producer_with_assigned_partition.send("registered_user_pert_partition", registered_user)
    pass


if __name__ == "__main__":
    while 1 == 1:
        registered_user = get_registered_user()
        print(registered_user)

        # single partition present in the topic
        # send_message_single_partition()

        # 2 partition is present in the topic
        send_message_multiple_partition()

        # Send message to perticular partition -> producers can be tightly couples to topic partitions
        #send_message_perticular_partition()

        time.sleep(4)
