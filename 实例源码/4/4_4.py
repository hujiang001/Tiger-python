#  author: Tiger，    wx ID：tiger-python
# file: ./4/4_4.py

# 列表
num_list1 = [10, 20, 30, 40]
num_list2 = [10, 20, 30, 40]

print('id(num_list1): %x, id(num_list2): %x' % (id(num_list1), id(num_list2)))

num_list1[0] = 50
print('num_list1: ', num_list1)

print('id(num_list1): %x, id(num_list2): %x' % (id(num_list1), id(num_list2)))
