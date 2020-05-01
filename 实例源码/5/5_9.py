#  author: Tiger，    wx ID：tiger-python
# file: ./5/5_9.py

# 集合 Set
set_1 = set('hello')
print(set_1)
print(len(set_1))

dict_1 = {}.fromkeys(set_1)  # 批量根据key值初始化一个字典
print(dict_1)

set_2 = frozenset('hello')  # 不可变集合
print(set_2)

# 新增元素
set_1.add('t')
print(set_1)
set_1.update('k', 'p')  # 批量添加多个
print(set_1)

# 删除元素
set_1.remove('t')
print(set_1)

# 判断元素是否存在
print('t' in set_1)
print('t' not in set_1)

# 清空元素
set_1.clear()
print(set_1)

# 集合操作
set_3 = set('hello')
set_4 = set('world')

print(set_3 - set_4)  # 补集
print(set_3 | set_4)  # 并集
print(set_3 & set_4)  # 交集
print(set_3 ^ set_4)  # 对称补集， 等同于 (set_3 - set_4) | (set_4 - set_3)

set_5 = {1, 2}
set_6 = {1, 2, 3}
print(set_5 < set_6)  # 子集判断
print(set_5 > set_6)  # 超集判断

