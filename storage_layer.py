"""
这是一个存储层，用来给用户接入存储
关键字 get（读），set（更新、插入），delete（删除）
使用的格式为：get key或者 set key value或 delete key
读取：若失败返回失败，成功返回1
本层根据用户的键，根据哈希算法把值分别存储到不同的结点
"""


import json

filename = 'data.json'


def get(key):
    """根据key读取数据"""
    with open(filename, 'r') as f_obj:
        datas = json.load(f_obj)
        if key in datas.keys():
            print(key + ': ' + datas[key])
        else:
            print("没有该关键字")


def set(key, value):
    """根据key，value插入或更新"""
    with open(filename, 'r+') as f_obj:
        datas = json.load(f_obj)
        f_obj.seek(0, 0)
        f_obj.truncate()
        datas[key] = value
        json.dump(datas, f_obj)


def delete(key):
    """根据key删除对应的key value"""
    with open(filename, 'r+') as f_obj:
        datas = json.load(f_obj)
        f_obj.seek(0, 0)
        f_obj.truncate()
        del_key = datas.pop(key)  # 返回删除的key
        print("已成功删除" + key + ": " + del_key)
        json.dump(datas, f_obj)


set('seven', '7')
