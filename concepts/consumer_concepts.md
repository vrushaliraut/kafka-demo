# Consumer 

```
Consumer -> consume from kafka partitions  -> internally consumer consume message from kafka topic partition
Every consumer is always assigned to consumer group

If no group_id is provided then random group id is assigned
configurations needed by consumer :-
topic, bootstrap_servers, group_id

Consumer group - logical grouping of one or more consumers,
It is mandatory for a consumer to registered itself to a consumer group
consumer instances are separate process ->
    - Consumer instance of same consumer group can be on different nodes
   consumer_offset - kafka interanaly stores the data for consumer consume the data 
   
// 1 partition and 1 consumer

// 1 topic 2 partitions 1 consumer  -> message will be consumed by C1 in round robin 

// 1 topic 1 partition 2 consumer  from same consumer group -> 
c1, c2 belongs to same consumer group -> kafka concept - same partition cant be assigned to multiple consumer in the same group 
 create 2 instance of consumer --> you can see whoever registered first that consumer will only get data 
from producer, so c2 is sitting ideal. 
 
// Different consumer group with consumer will get data

* Multiple partition and multiple consumer :- 
Both consumer are registered to same consumer group
c1 -> p0 (topic), c2 -> p1  (topic)

  

```


