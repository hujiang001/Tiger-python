#  author: Tiger，    wx ID：tiger-python
# file: ./6/6_2.py

# bytes 按照16进制输出，强制不ascii转码
def trans(s):
    return "b'%s'" % ''.join('\\x%.2x' % x for x in s)


# 字节序
byte_1 = 'python'.encode('utf-8')
print(trans(byte_1))
print('Big endian: ', hex(int.from_bytes(byte_1, byteorder='big', signed=False)))
print('Little endian: ', hex(int.from_bytes(byte_1, byteorder='little', signed=False)))

# 获取当前cpu的字节序类型
import sys
print('endian of cur env:', sys.byteorder)
