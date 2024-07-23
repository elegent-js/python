# 转换并同时计算数据
# 问题：需要在数据序列上执行聚集函数（比如 sum()、min()、max()），但是首先需要先转换或者过滤数据
# 解决方案：一个非常优雅的方式去结合数据计算与转换就是使用一个生成器表达式参数
# 生成器表达式非常重要，可以简化代码，提高可读性。格式：(expr for val in collection if condition)
import os

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)

# Determine if any .py files exist in a directory
files = os.listdir('.')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
