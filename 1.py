import json

filename = 'data.json'

# 更新或者插入
with open(filename, 'r+') as f_obj:
    datas = json.load(f_obj)
    f_obj.seek(0, 0)
    f_obj.truncate()
    key = input("请输入key：")
    value = input("请输入value: ")
    datas[key] = value
    print(datas, type(datas))
    json.dump(datas, f_obj)
