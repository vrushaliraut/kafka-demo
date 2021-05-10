This repo is created with respect to understand kafka broker and consumer and sceanarios with producers and consumers 

Notes taken while playing with multiple versions :- 

Kafka zookeeper :- 
2181 -> use machine ip

Kafka broker/ kafka server  -> 9092
advertised.listener  = <machine.ip>:9092
zookeeper.connect = <machine.ip>:2181

Zookeeper :- 

zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties
bin/zookeeper-server-start.sh config/zookeeper.properties

Kafka server :-

Troubleshooting 1  - Address already in use 
lsof -n -i :9092 | grep LISTEN
kill -9 76271

Troubleshooting 2  - failed to aquired lock kafka -logs

Fatal error during KafkaServer startup. Prepare to shutdown (kafka.server.KafkaServer)
org.apache.kafka.common.KafkaException: Failed to acquire lock on file .lock in /usr/local/var/lib/kafka-logs. A Kafka instance in another process or thread is using this directory.

cd /usr/local/var/lib/kafka-logs
rm -rf kafka-logs

sudo rm -rf /usr/local/var/lib/kafka-logs


Troubleshooting 3 
Error while creating ephemeral at /brokers/ids/0, node already exists and owner '72060234671915022' does not match current session '72060234671915024' (kafka.zk.KafkaZkClient$CheckedEphemeral)
[2021-05-10 11:38:57,415] ERROR [KafkaServer id=0] Fatal error during KafkaServer startup. Prepare to shutdown (kafka.server.KafkaServer)
org.apache.zookeeper.KeeperException$NodeExistsException: KeeperErrorCode = NodeExists


kafka-server-stop


Kafka - /usr/local/etc/kafka
Logs  - /usr/local/var/lib/

JMX_PORT=8004 kafka-server-start server.properties
JMX_PORT=8004 bin/kafka-server-start.sh config/server.properties


How to check connection is successful :- 
INFO Creating new log file: log.380a (org.apache.zookeeper.server.persistence.FileTxnLog)


CMAK :- Kafka manager 

./sbt clean dist 
cd target 
cd universal 
	Unzip cmak.tar
	Cmak folder -> cd conf -> vim application.conf
 
	Path where cmak is installed :- 
/usr/local/var/lib/CMAK/target/universal/cmak-3.0.0.5

 bin/cmak -Dconfig.file=conf/application.conf -Dhttp.port=8080


**********************************
Kafka 2.8.0 - kafka without zookeeper - 
Raft protocol -> Kraft protocol  - 

cd /Users/vrushali/kafka-2.8.0-src


Cd kafka-2.8.0-src
 
zookeeper-server-start  config/zookeeper.properties 

kafka-server-start config/server.properties

Create topic - 
kafka-topics --create --topic quickstart-events --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1


Describe topic :- 
kafka-topics --describe --topic quickstart-events --bootstrap-server localhost:9092

Topic:quickstart-events	PartitionCount:1	ReplicationFactor:1	Configs:segment.bytes=1073741824
	Topic: quickstart-events	Partition: 0	Leader: 0	Replicas: 0	Isr: 0

5 Nodes 

1,3,5 - controller 
2, 4  - broker 

*****************************************************************************************

Server.properties 

/usr/local/etc/kafka/kafka_2.12-2.6.1/config

Machine IP address :- 

address X.X.0.X - local machine ip

zookeeper.connect=X.X.0.X:2181
advertised.listeners=PLAINTEXT://X.X.0.X:9092

Zookeeper 
bin/zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties

Kafka 

JMX_PORT=8004 bin/kafka-server-start.sh config/server.properties

CMAK 
Git clone https://github.com/yahoo/CMAK.git
Ls- cMAC sbt -> ./sbt clean dist 
Cd target -> cd universal -> unzip cmak.tar -> cmak folder -> cd conf 
Vim application.conf 
Cmak.zkhosts = “machineip:2181”

Start cMAK 
/usr/local/etc/kafka/kafka_2.12-2.6.1/CMAK/target/universal/cmak-3.0.0.5 

What are kafka topic partitions  :- 

Concepts of kafka producers :- 
Single broker with 1 partition 
1 topic 1 broker 
registered_user -  all the data was going to single partition in the topic

1 Topic 2 partitions 1 broker 
When 2 partitions are present for a single topic, message publish is random. 
Message publish happens randomly. 

Kafka producer send message to single topic partition 
key_bytes
all_partiition
available_partition
available_partition
