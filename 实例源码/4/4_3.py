#  author: Tiger，    wx ID：tiger-python
# file: ./4/4_3.py

score1 = 10
print('id(score1): %x' % (id(score1)))

score2 = score1
print('id(score2): %x' % (id(score2)))

score1 = 20
print('id(score1): %x, id(score2): %x, ' % (id(score1), id(score2)))

print('score1: ', score1)
print('score2: ', score2)
