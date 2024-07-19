# 实现字典排序
from collections import OrderedDict

# 会按插入顺序打印, 相当于java中的LinkedHashMap，使用一个单独的链表维护元素的插入顺序
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])
print("*" * 20)

# 对比普通的字典,
d = {'bar': 2, 'foo': 1, 'spam': 3, 'grok': 4}
for key in d:
    print(key, d[key])

