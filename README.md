# python


## tuple (元组)
不可变的列表即为元组

## 使用*接收可变参数列表

## 使用**接收字典

## 类

## list comprehensions(列表生成式)
```py
[x * x for x in range(1, 11) if x % 2 == 0]
```

## generator
```py
g = (x * x for x in range(1, 10000))
next(g)
next(g)
```