### Replication

* Fault tolerant
* Each partition is replicated across multiple server for fault tolerant
* Only one partition will be replicate message and called followers
* Other partition will only replicate message and called followers 
* The leader handles all read and write request for the partition while followers passively replicate the leader