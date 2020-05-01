#  author: Tiger，    wx ID：tiger-python
# file: ./5/5_10.py

# 深复制和浅复制
dict_1 = {'name': 'xiaowang', 'age': 20, 'score': {'yuwen': 90, 'shuxue': 100}}
dict_2 = dict_1.copy()

print('dict_1:', dict_1)
print('dict_2:', dict_2)

# 修改value
print('modify 90->98'.center(64, '-'))
dict_1['score']['yuwen'] = 98
print('dict_1:', dict_1)
print('dict_2:', dict_2)

# 深拷贝
print('deep copy'.center(64, '-'))

import copy
dict_3 = copy.deepcopy(dict_1)
print('dict_1:', dict_1)
print('dict_3:', dict_3)
print('modify 98->99'.center(64, '-'))
dict_1['score']['yuwen'] = 99
print('dict_1:', dict_1)
print('dict_3:', dict_3)


