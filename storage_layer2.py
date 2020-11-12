"""
这是服务器2的存储层，用来存储或读取用户数据
关键字 get（读），set（更新、插入），delete（删除）
使用的格式为：get key或者 set key value或 delete key
读取：若失败返回失败，成功返回1
"""


import json

filename = 'data2.json'


def get_k(key):
    """根据key查找读取数据"""
    with open(filename, 'r') as f_obj:
        datas = json.load(f_obj)
        if key in datas.keys():
            print(key + ': ' + datas[key])
        else:
            print("没有该关键字！")


def set_kv(key, value):
    """根据key，value插入或更新"""
    with open(filename, 'r+') as f_obj:
        datas = json.load(f_obj)
        f_obj.seek(0, 0)
        f_obj.truncate()
        datas[key] = value
        json.dump(datas, f_obj)
        print("成功更改！")


def delete_k(key):
    """根据key删除对应的key value"""
    with open(filename, 'r+') as f_obj:
        datas = json.load(f_obj)
        f_obj.seek(0, 0)
        f_obj.truncate()
        del_key = datas.pop(key)  # 返回删除的key
        print("已成功删除" + key + ": " + del_key)
        json.dump(datas, f_obj)
