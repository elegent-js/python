# 从不定数量的集合中赋值给固定的变量
import numpy as np


# 从不定数量的集合中赋值给固定的变量, *middle 会是一个列表
def drop_first_last(grades):
    first, *middle, last = grades
    return np.mean(middle)


avg_val = drop_first_last([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(avg_val)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)

# 用星号表达式迭代元素为可变长度的元组序列
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


# 字符串分割
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)
print(*fields)


# 分割列表
#items = [1, 10, 7, 4, 5, 9]
#head, *tail = items
#print(head)
#print(tail)


# 使用递归求和
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head


val = sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(val)


