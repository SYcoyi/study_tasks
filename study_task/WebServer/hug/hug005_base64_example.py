import base64

# raw = "just a string"
# encoded = base64.b64encode(raw.encode("utf-8"))   # python中的base64要求传入的参数类型为bytes
# decoded = base64.b64decode(encoded)
# print(raw)
# print(type(raw))
# print()
# print(raw.encode("utf-8"))
# print(type(raw.encode("utf-8")))    # <class 'bytes'>
# print()
# print(encoded)
# print(decoded)
# print()
# print(decoded.decode())
# print(type(decoded.decode()))    # <class 'str'>
# print()
# print(decoded.decode("utf-8"))
# print(type(decoded.decode("utf-8")))     # <class 'str'>

"""
第二行，在进行base64编码前，先对raw进行了utf-8编码。 utf-8编码是把数据类型从字符串(str)转换成字节码(bytes)
因为base64的python实现要求传输的参数类型是bytes
decoded.decode("utf-8")：对utf-8编码的bytes进行解码，解码为字符串str
"""

# # 不指定字符集
# b1 = b'I love U.'          # <class 'bytes'>
# b11 = u'没打印出来前面的u'     # <class 'str'>
# b111 = "就是字符串"
# print("b1 type: ", type(b1))   # <class 'bytes'>
# print("b11 type:", type(b11))  # <class 'str'>
# print(b1)   # b'I love U.'   注意前面打印有个b
# print(b11)   # 没打印出来前面的u
# print(b111)
# print(b1[:-3])  # 从后开始数，前含后不含
# print(b1[:3])
# print(b11[:-3])
# print(b111[:3])

# # 指定字符集
# b2 = bytes('爱你哟', encoding='UTF-8')    # 字节 <class 'bytes'>
# b22 = bytes('爱你哟', encoding='UTF-8')
# print(type(b2))
# print('b2', b2)

# 字符串转为bytes
raw2 = "test_user:test_password"
raw2_encoded = base64.b64encode(raw2.encode('utf-8'))   # b'dGVzdF91c2VyOnRlc3RfcGFzc3dvcmQ='
print(raw2_encoded)
raw2_decoded = base64.b64decode(raw2_encoded)    # b'test_user:test_password'
print(raw2_decoded)
aa = raw2_decoded.decode('utf-8')   # 将bytes格式的再解码为str格式
print(aa)
