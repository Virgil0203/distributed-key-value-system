"""
这是一个哈希路由模块
要把用户的key，根据哈希值，散列到不同的服务器
"""


import storage_layer1
import storage_layer2


def hash_get(key):
    """根据key来散列到不同的服务器, 执行get"""
    if int(key) <= 500:
        storage_layer1.get_k(key)  # 实际要把key传到服务器，并调用此函数
    else:
        storage_layer2.get_k(key)


def hash_set(key, value):
    """根据key来散列到不同的服务器，执行set"""
    if int(key) <= 500:
        storage_layer1.set_kv(key, value)
    else:
        storage_layer2.set_kv(key, value)


def hash_del(key):
    """根据key来散列到不同的服务器，执行del"""
    if int(key) <= 500:
        storage_layer1.delete_k(key)
    else:
        storage_layer2.delete_k(key)
