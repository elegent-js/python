# 使用Python实现一个优先队列

import heapq


class PriorityQueue:
    """
    定义优先级队列类，采用heapq模块实现
    """

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    """
    定义一个Item类，用于测试优先级队列
    """

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

print(q.pop())  # Item('bar')
print(q.pop())  # Item('spam')
