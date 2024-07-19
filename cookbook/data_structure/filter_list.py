# 过滤序列元素
# 最简单的过滤序列元素的方法就是使用列表推导式
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
# 列表推导式，过滤出大于0的元素
sublist = [n for n in mylist if n > 0]
print(sublist)

# 使用生成器表达式迭代过滤，可减少内存消耗
pos = (n for n in mylist if n > 0)
for x in pos:
    print(x)


values = ['1', '2', '-3', '-', '4', 'N/A', '5']




def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(lambda e: is_int(e), values))
print(ivals)



# compress()函数，根据一个布尔序列去过滤一个序列
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
from itertools import compress
more5 = [n > 5 for n in counts]
print(more5)

print(list(compress(addresses, more5)))
