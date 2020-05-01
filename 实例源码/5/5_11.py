#  author: Tiger，    wx ID：tiger-python
# file: ./5/5_11.py

'''
数据类型转换
'''

# 转换为int
print('int'.center(30, '*'))
print(int(1.2))  # float -> int
print(int('123'))  # string -> int
print(int(True))  # bool -> int

# 转换为float
print('float'.center(30, '*'))
print(float('1.2'))  # string->float
print(float(123))  # int->float
print(float(False))  # bool->float

# 所有基本类型都可以转换为bool
print('bool'.center(30, '*'))
print(bool(1))  # int->bool
print(bool(0.0))  # float->bool
print(bool(0 + 0j))  # complex->bool
print(bool(''))  # string->bool, 空字符串为False,其它都是True
print(bool([]))  # list->bool, 空为False,其它都是True
print(bool(()))  # tuple->bool, 空为False,其它都是True
print(bool({}))  # dict->bool, 空为False,其它都是True
print(bool(set()))  # set->bool, 空为False,其它都是True

# 转换为complex
print('complex'.center(30, '*'))
print(complex(100))  # int->complex
print(complex(1.2))  # float->complex
print(complex(True))  # bool->complex
print(complex('1.2+2.3j'))  # string->complex

# 所有基本类型都可以转换为string
print('string'.center(30, '*'))
print(str(1))  # int->string
print(str(1.2))  # float->string
print(str(True))  # bool->string
print(str(1.2 + 2.3j))  # complex->string其它都是True
print(str(['hello', 100]))  # list->string
print(str(('hello', 100)))  # tuple->string
print(str({'name': 'xiaowang', 'age': 20}))  # dict->string
print(str({'name', 'age'}))  # set->string

# 转换为list
print('list'.center(30, '*'))
print(list("hello"))  # string->list
print(list((100, 200, 300)))  # tuple->list
print(list({'name', 'age'}))  # set->list
print(list({'name': 'xiaowang', 'age': 20}))  # dict->list， 只取key值

# 转换为tuple
print('tuple'.center(30, '*'))
print(tuple("hello"))  # string->tuple
print(tuple([100, 200, 300]))  # list->tuple
print(tuple({'name', 'age'}))  # set->tuple
print(tuple({'name': 'xiaowang', 'age': 20}))  # dict->tuple， 只取key值

# 转换为set
print('set'.center(30, '*'))
print(set("hello"))  # string->set
print(set([100, 200, 300]))  # list->set
# print(set([100, 200, [300, 400]]))  # list->set, list中包含可变数据类型，报异常
print(set(('name', 'age')))  # tuple->set
# print(set(('name', 'age', [])))  # tuple->set,包含可变数据类型，报异常
print(set({'name': 'xiaowang', 'age': 20}))  # dict->set， 只取key值

# 转换为dict的方法略微复杂一些
print('dict'.center(30, '*'))

# string->dict
user_str = '{"name": "xiaowang", "city": "Chengdu", "age": 28}'
import json
print(json.loads(user_str))  # 方式一、使用json转换，字符串格式需要严格按照json格式来
print(eval(user_str))  # 方式二、使用eval函数转换，eval有安全隐患，不建议使用
import ast
print(ast.literal_eval(user_str))  # 方式三、 使用ast.literal_eval

# list->dict
user_keys = ['name', 'city', 'age']
user_values = ['xiaowang', 'Chengdu', 28]
print(dict(zip(user_keys, user_values)))  # 方式一、需要用到zip

user_info = [
    ["name", "xiaowang"],
    ["city", "Chengdu"],
    ["age", 28]
    ]
print(dict(user_info))  # 方式二、二维列表


# set->dict tuple->dict的方式和list->dict一样
