#  author: Tiger，    wx ID：tiger-python
# file: ./6/6_3.py

# bytes 按照16进制输出，强制不ascii转码
def trans(s):
    return "b'%s'" % ''.join('\\x%.2x' % x for x in s)


# 字符编码
encstr_1 = 'tiger-python'
encbytes_1 = encstr_1.encode('utf-8')
print(trans(encbytes_1))
print(encbytes_1.decode('utf-16'))  # 编码方式不一致，造成乱码
print(encbytes_1.decode('utf-8'))
