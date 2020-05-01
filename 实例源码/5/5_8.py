#  author: Tiger，    wx ID：tiger-python
# file: ./5/5_8.py

# 字典
dict_1 = {'name': 'xiaowang', 'age': 20, 'city': 'Chengdu'}
print('name: %s, age: %d, city: %s' % (dict_1['name'], dict_1['age'], dict_1['city']))

dict_1['city'] = 'Beijing'
print('name: %s, age: %d, city: %s' % (dict_1['name'], dict_1['age'], dict_1['city']))

dict_2 = {}.fromkeys(('name', 'age', 'city'))  # 批量根据key值初始化一个字典
print(dict_2)

print(len(dict_1))

# 增加键值对
dict_1['sex'] = 'male'
print(dict_1)

# 删除键值对
del dict_1['sex']
print(dict_1)

# 批量更新
dict_3 = {'name': 'xiaoliu', 'age': 18, 'city': 'Chengdu', 'sex': 'female'}
dict_1.update(dict_3)
print(dict_1)

# 判断key是否在字典中存在
print('name' in dict_3)

# 获取所有的key
print(list(dict_1.keys()))

# 获取所有的value
print(list(dict_1.values()))

# 获取所有的(键, 值) 元组列表
print(list(dict_1.items()))

# 清空字典
dict_1.clear()
print(dict_1)
