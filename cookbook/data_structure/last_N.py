# 保留最后N个元素：在迭代或其他操作的时候，怎么样只保留最后有限几个元素的历史记录
# 使用collections.deque可以构造一个固定大小的队列，当新的元素加入并且这个队列已满的时倍，最老的元素会自动被移除掉

from collections import deque


def search(lines, pattern, history=5):
    """
    保留最后N个元素
    """
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


with open('somefile.txt') as f:
    for line, prevlines in search(f, 'python', 5):
        for pline in prevlines:
            print(pline, end='')
        print(line, end='')
        print('-'*20)



# 演示deque的用法
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
