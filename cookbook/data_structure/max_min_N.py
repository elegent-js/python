# 查找最大或最小的N个元素

import heapq


nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# 找出最大的3个数
print(heapq.nlargest(3, nums))  # Prints [42, 37, 23]

# 找出最小的3个数
print(heapq.nsmallest(3, nums))  # Prints [-4, 1, 2]


# 也可以传入一个key参数，用于更复杂的数据结构
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

# 找出最贵的3个股票
expensive = heapq.nlargest(3, portfolio, key=lambda e: e['price'])
cheap = heapq.nsmallest(3, portfolio, key=lambda e: e['price'])

print(expensive)
print(cheap)

# heapq模块的nlargest()和nsmallest()函数适合在相对小的数据集中查找最大或最小的N个元素
# 如果N的大小和集合大小接近的时候，通常更快的方法是先对集合排序，然后做切片操作
# sorted(items)[:N] 或者 sorted(items)[-N:]
# 但是，如果N的大小和集合大小差别很大，那么nlargest()和nsmallest()函数更合适
# 因为在底层实现中，nlargest()和nsmallest()函数会先将集合数据进行堆排序后放入一个列表中
# 所以，nlargest()和nsmallest()函数的时间复杂度是O(NlogN)，而sorted(items)[:N]的时间复杂度是O(NlogN)
# 所以，nlargest()和nsmallest()函数更适合于N相对较小的情况
# 如果N和集合大小差别很大，那么先排序再切片更合适

# 取最大元素
print(max(nums))
# 取最小元素
print(min(nums))
# 取最大N个元素（N较小时）
print(heapq.nlargest(3, nums))
# 取最大N个元素（N较大时）
print(sorted(nums, reverse=True)[:3])
# 使用heap结构取出最小的元素
heap = list(nums)
heapq.heapify(heap)
print(heapq.heappop(heap))


