# distributed-key-value-system

Overall requirements: save each data object (as a binary data stream) not larger than 4M,
and design the key implementation scheme by yourself.
Storage nodes are several computers on the local area network or several virtual machines on the same host machine, 
and you can use any operating system.These nodes are connected based on LibP2P. 
You can refer to IPFS, FileCoin, Storj, etc.,
but you cannot copy it directly, and you must expand the key/value storage on the LibP2P peer node.
