# 字典的运算：min, max, sort。 etc.
# 这里用到内置的zip函数，将字典的key和value反转，然后再进行比较。
# zip函数返回的是一个迭代器，需要用list()转换成列表。

# zip函数的使用
# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象。
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
zipped = zip(list1, list2)
print(list(zipped))

# 解压
zipped = [(1, 'a'), (2, 'b'), (3, 'c')]
list11, list12 = zip(*zipped)
print(list11)
print(list12)

price = {
    'apple': 10,
    'banana': 5,
    'orange': 20,
    'grape': 15,
}

# 最大值
max_price = max(zip(price.values(), price.keys()))
print(max_price)

# 生成器表达式(generator expression)
gen = (x ** 2 for x in range(10))
print(list(gen))

# 列表推导式（list comprehension）
gen = [x ** 2 for x in range(10)]
print(gen)