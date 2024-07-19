# 使用reg_exp.split()方法分割字符串
import re
line = 'asdf     fjdk; afed, fjek,asdf, foo'
result = re.split(r'[;,\s]\s*', line)
print(result)

