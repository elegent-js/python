#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 演示编解码
# str -> bytes, bytes -> str

# 编码
print('abc'.encode('ascii')) 
print('中文'.encode('utf-8'))

# 解码
print(b'abc'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 打印字符串长度
print(len('abc'))

# 打印bytes长度
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
