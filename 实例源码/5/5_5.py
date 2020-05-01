#  author: Tiger，    wx ID：tiger-python
# file: ./5/5_5.py

"""
演示列表的操作
"""

# list 列表
list_1 = ['hello', 100, ['跟我一起学', 4]]  # 支持不同类型的item，可以嵌套list
list_2 = ['python', '!']

print(list_1[0:2])  # 截取的方式和字符串一致
print(list_1[0:-2])
print(list_1[0: 1])
print(list_1[0])

print(len(list_1))  # 获取列表的长度

# 列表连接
list_3 = list_1 + list_2
print(list_3)

# 使用乘法让列表重复n次
list_4 = list_2 * 3
print(list_4)

# 判断一个元素是否存在于列表中
print('python' in list_2)  # True
print('python' not in list_2)  # False

# 判断一个元素在列表中出现的次数
print(list_4.count('python'))

# 获取列表中最大最小值,求和
list_5 = [1, 2, 4, 10, 90]
print(max(list_5))
print(min(list_5))
print(sum(list_5))

# 列表的增删改操作
list_5.append(100)  # 在列表尾增加元素100
print(list_5)

list_5.insert(1, 'insert_obj')  # 把元素插入到索引为1的位置
print(list_5)

list_6 = ['hello', 'python']
list_5.extend(list_6)  # 在列表后面追加另外一个列表

list_5[0] = 200  # 将索引为0的元素修改为200
print(list_5)

del list_5[0]  # 删除索引为0的元素
print(list_5)

list_5.pop(2)  # 移除索引为2的元素，如果不填写索引值，则默认移除列表最后一个元素
print(list_5)

list_5.remove('insert_obj')  # 移除一个元素，注意这里指定的是元素的值。如果列表中有多个相同的值，则只移除第一个匹配项
print(list_5)

list_5.clear()  # 清空整个列表
print(list_5)

# 列表的排序操作
list_7 = [100, 99, 27, 198, 3]

list_7.reverse()  # 列表反向排列
print(list_7)

list_7.sort()  # 列表升序排列
print(list_7)

list_7.sort(reverse=True)  # 列表降序排列
print(list_7)







