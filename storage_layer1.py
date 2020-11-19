"""
这是服务器1的存储层，用来存储或读取用户数据
关键字 get（读），set（更新、插入），delete（删除）
使用的格式为：get key或者 set key value或 delete key
读取：若失败返回失败，成功返回1
"""


import json
import os
from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn


class ThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass


def get_k(key):
    """根据key查找读取数据"""
    chunkNum = int(key) // 80000 + 1
    chunkName = 'chunk_' + str(chunkNum) +'.json'
    if os.path.exists(chunkName):
        with open(chunkName, 'r') as f_obj:
            datas = json.load(f_obj)
            if key in datas.keys():
                info = key + ': ' + datas[key]
                return info
            else:
                info = "没有该关键字！"
                return info
    else:
        info = "没有该关键字！"
        return info


def set_kv(key, value):
    """根据key，value插入或更新"""
    chunkNum = int(key) // 80000 + 1
    chunkName = 'chunk_' + str(chunkNum) +'.json'
    if os.path.exists(chunkName):
        with open(chunkName, 'r+') as f_obj:
            datas = json.load(f_obj)
            f_obj.seek(0, 0)
            f_obj.truncate()
            datas[key] = value
            json.dump(datas, f_obj)
            info = "成功更改！"
            return info
    else:
        os.mknod(chunkName, 0o777)
        textData = {'text': 'avoid error'} # 写入一个文本数据防止解析json出错
        with open(chunkName, 'r+') as f_obj:
            json.dump(textData, f_obj)

        with open(chunkName, 'r+') as f_obj:
            datas = json.load(f_obj)
            f_obj.seek(0, 0)
            f_obj.truncate()
            datas[key] = value
            json.dump(datas, f_obj)
            info = "成功更改！"
            return info


def delete_k(key):
    """根据key删除对应的key value"""
    chunkNum = int(key) // 80000 + 1
    chunkName = 'chunk_' + str(chunkNum) +'.json'
    if os.path.exists(chunkName):
        with open(chunkName, 'r+') as f_obj:
            datas = json.load(f_obj)
            if key in datas.keys():
                f_obj.seek(0, 0)
                f_obj.truncate()
                del_key = datas.pop(key)  # 返回删除的key
                info = "已成功删除" + key + ": " + del_key
                json.dump(datas, f_obj)
                return info
            else:
                info = "不存在！"
                return info
    else:
        info = "不存在！"
        return info


if __name__ == '__main__':
    server1 = ThreadXMLRPCServer(('192.168.18.128', 8888)) # 初始化
    server1.register_function(get_k, "get") # 注册函数
    server1.register_function(set_kv, "set") # 注册函数
    server1.register_function(delete_k, "delete") # 注册函数
    print("Server1 is Listening for Client...")
    server1.serve_forever() # 保持等待调用状态
