"""
这是一个哈希路由模块
要把用户的key，根据哈希值，散列到不同的服务器
"""


# import storage_layer1
# import storage_layer2
from xmlrpc.client import ServerProxy



# if __name__ == '__main__':
server1 = ServerProxy("http://192.168.18.128:8888") # 初始化服务器
server2 = ServerProxy("http://192.168.18.129:8888") # 初始化服务器


def hash_get(key):
    """根据key来散列到不同的服务器, 执行get"""
    if int(key) <= 2000000:
        print(server1.get(key))
        # storage_layer1.get_k(key)  # 实际要把key传到服务器，并调用此函数
    elif int(key) <= 4000000:
        # storage_layer2.get_k(key)
        print(server2.get(key))
    else:
        print("您只可以查找key为4,000,000以下的键值对！")


def hash_set(key, value):
    """根据key来散列到不同的服务器，执行set"""
    if int(key) <= 2000000:
        print(server1.set(key, value))
       # storage_layer1.set_kv(key, value)
    elif int(key) <= 4000000:
       # storage_layer2.set_kv(key, value)
       print(server2.set(key, value))
    else:
        print("您只可以存储key为4,000,000以下的键值对！")


def hash_del(key):
    """根据key来散列到不同的服务器，执行del"""
    if int(key) <= 2000000:
        print(server1.delete(key))
        # storage_layer1.delete_k(key)
    elif int(key) <= 4000000:
        # storage_layer2.delete_k(key)
        print(server2.delete(key))
    else:
        print("您只可以删除key为4,000,000以下的键值对！")

