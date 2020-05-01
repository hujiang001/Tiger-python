#  author: Tiger，    wx ID：tiger-python
# file: ./5/5_7.py

# 元组的操作
tuple_1 = (1, 2, 100, 'python')
tuple_2 = 'hello', 'python', 100  # python中，未加括号的序列都默认是元组
tuple_3 = (98,)  # 只包含一个元素的元组，需要加上逗号，否则小括号会被认为是运算符

# 元组的元素不可改变
tuple_4 = (1, 5, 10)
# tuple_4[0] = 3  # 会抛出异常
print(id(tuple_4))
tuple_4 = (100, 99)
print(tuple_4)
print(id(tuple_4))

# 元组的元素可以是可变数据类型
tuple_5 = (100, 200, [300, 400])
tuple_5[2][0] = 500
print(tuple_5)


