#  author: Tiger，    wx ID：tiger-python
# file: ./5/5_4.py

"""
演示字符串操作
"""

# 转义字符
str1 = 'hello,\nworld!'
# 尾部的\是续行符，表示下一行也算作本行的内容。续行符后面不能再有任何字符，包括空格和注释
str2 = 'hello,\"world!\"' \
       'I am Tiger.'

print(str1)
print(str2)

# 字符串截取
str3 = 'hello, world!'
sub_str1 = str3[0:5]  # 截取 hello
sub_str2 = str3[-6:-1]  # 截取 world
print(sub_str1)
print(sub_str2)
print(str3[5])  # 输出第6个字符
print(str3[:5])  # 输出第6个字符之前的所有字符
print(str3[5:])  # 输出第6个字符及以后的所有字符
print(str3[-5:])  # 输出倒数第5个字符及以后的所有字符

# 字符串分割 split
sub_str_list = str3.split(',')
print(sub_str_list)
print(str3.split('o'))
print(str3.split('o', 1))

# 字符串连接
str4 = ' I am Tiger.'
print(str3 + str4 + " Glad to see you ! ")
print('my'.join([str3, str4, " Glad to see you ! "]))

print('**'.join(["aa", "bb", "cc"]))  # aa**bb**cc

# 字符串替换
str5 = 'python'
print(str3.replace('world', str5))
print(str3.replace('l', 't'))  # 将l替换为t，不限制替换次数
print(str3.replace('l', 't', 2))  # 将l替换为t，限制最多替换2次

# 字符串查找
str6 = 'hello, python'
sub_str_find = 'll'
sub_str_not_find = 'world'
print(str6.find(sub_str_find))  # ‘ll’匹配到str6的起始索引是2，所以返回2
print(str6.find(sub_str_find, 3))  # 指定从str6的索引为3开始，所以查找不到，返回-1
print(str6.find(sub_str_not_find))  # world字符串不在str6里面，返回-1

print(str6.index(sub_str_find))  # ‘ll’匹配到str6的起始索引是2，所以返回2
# print(str6.index(sub_str_find, 3))  # 指定从str6的索引为3开始，所以查找不到，抛出一个异常

str7 = 'hello, python, hello'
print(str7.find('ell'))  # 正向查找，返回第一次查找到的索引
print(str7.rfind('ell'))  # 反向查找，返回第一次查找到的索引


# 格式化输出
fmt_1ist = [10.2, 99, 'hello']
print('this is example for fmt output \n %.4f, %#0x, %10s' % (fmt_1ist[0], fmt_1ist[1], fmt_1ist[2]))

# str.format
print('this is example for fmt output \n {:.4f}, 0x{:x}, {:>10}'.format(fmt_1ist[0], fmt_1ist[1], fmt_1ist[2]))




