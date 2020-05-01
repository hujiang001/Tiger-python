#  author: Tiger，    wx ID：tiger-python
# file: ./6/6_1.py

# bytes 按照16进制输出，强制不ascii转码
def trans(s):
    return "b'%s'" % ''.join('\\x%.2x' % x for x in s)


# bytes类型
bytes_1 = bytes('hello', 'utf-8')
bytes_2 = bytes([1, 200, 80, 50])
bytes_3 = b'world'
bytes_4 = b'\x77\x6f\x72\x6c\x64'


print('bytes_1:', bytes_1)
print('bytes_2:', bytes_2)
print('type of bytes_1:', type(bytes_1))
print('bytes_1:', trans(bytes_1))
print('bytes_2:', trans(bytes_2))
print('bytes_3:', trans(bytes_3))
print('bytes_4', bytes_4)

# 操作方法
print(bytes_3[0: 3])
print(bytes_1 + bytes_3)
print(b'h' in bytes_1)
print(bytes_1.split(b'l'))
print(bytes_1.find(b'll'))
print(bytes_1.replace(b'l', b't'))

# 不可变类型
# bytes_3[0] = b'k' # 报错
