#  author: Tiger，    wx ID：tiger-python
# file: ./4/4_2.py

score1 = 10
score2 = 50

# score1 score2的地址
print('id(score1): %x, id(score2): %x, ' % (id(score1), id(score2)))

score2 = score2 - score1

# 字符串打印
print('score2: ', score2)

print('score2')

# score1 score2的地址
print('id(score1): %x, id(score2): %x, ' % (id(score1), id(score2)))

score3 = 40
print('id(score3): %x' % (id(score3)))
