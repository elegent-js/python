# 通过某个关键字排序一个字典列表

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows = sorted(rows, key=lambda x: [x['fname'], x['uid']])
print(rows)

# 通过使用 operator 模块的 itemgetter 函数，可以更快的实现
from operator import itemgetter
rows = sorted(rows, key=itemgetter('fname', 'uid'))
print(rows)