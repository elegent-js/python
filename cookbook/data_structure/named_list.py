# 映射名称到序列元素
from collections import namedtuple

# 定义一个命名元组
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
list = [
    ["hello", "world", "python"]
]
for record in list:
    s = Stock(*record)
    print(s.name, s.shares, s.price)