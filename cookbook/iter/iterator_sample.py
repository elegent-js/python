# 手动遍历迭代器
from datetime import datetime


def manual_iter():
    with open('iterator_sample.py') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            return


manual_iter()


# 对列表施加iter()函数，返回一个迭代器对象
items = [1, 2, 3]
it = iter(items)
print([i for i in it])


# 代理迭代
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    for ch in root:
        print(ch)


# 使用生成器创建新的迭代模式，需要使用生成器函数来实现
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


start = datetime.now()
for n in frange(0, 10000, 100):
    print(n)
end = datetime.now()

diff = end - start

print('cost Time:', diff.total_seconds(), 's')


# 反向迭代
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


for rr in reversed(Countdown(10)):
    print(rr)

print("*" * 20)

for rr in Countdown(10):
    print(rr)

