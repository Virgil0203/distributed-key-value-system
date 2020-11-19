"""
这是前端层
提供给用户使用接口
包括关键字：get（读），set（写、更新），delete（删除）
本层根据用户的键，根据哈希算法把值分别存储到不同的结点
无限循环，反复询问用户操作，直到用户想退出
"""


import hash_route

info = True
while info:
    keyword = input("请输入get或set或delete（退出请键入q）: ")
    if keyword == 'q':
        info = False

    if keyword == 'get':
        key = input("\n请输入key:")
        hash_route.hash_get(key)

    if keyword == 'set':
        key, value = input('请输入key value，用空格隔开: ').split(' ')
        hash_route.hash_set(key, value)

    if keyword == 'delete':
        key = input('请输入要删除的key: ')
        hash_route.hash_del(key)
