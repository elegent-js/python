# python
learning python

### 重要知识点

##### 1. 生成器表达式 (Generator Expression)
```python
# 生成器表达式
gen = (x ** 2 for x in range(10))
print(list(gen))  

# result: 
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

注意：生成器表达式返回的是一个迭代器（生成器对象），并不是列表


##### 2. 列表推导式 (List Comprehension)
```python
# 列表推导式
lst = [x ** 2 for x in range(10)]
print(lst)

#result:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
注意区别：列表推导式返回的是一个列表，生成器表达式返回的是一个迭代器（生成器对象）

##### 3. yield
yield 是一个类似 return 的关键字，只是这个函数返回的是个生成器。yield 语句每次执行时，立即返回结果给调用者，而当前的状态仍然保留，以便迭代器下一次循环调用。
yield有产生的意思

它在Python中用于定义生成器函数。生成器函数是一种特殊的函数，它可以暂停执行并在需要时恢复，从而一次生成一个值。这使得yield在处理大型数据集或需要惰性求值的情况下特别有用。

###### 3.1 生成器函数
```python
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

# It returns an object but does not start execution immediately.
a = [i for i in my_gen()]
print(a)


```
原理：
暂停执行：每当生成器函数遇到 yield 时，它会暂停执行并返回 yield 后面的值。生成器函数的状态会被保留，以便下次调用时继续执行。
恢复执行：当再次调用生成器对象的 __next__() 方法时，生成器函数会从上次暂停的地方继续执行。直到下一个 yield 语句或函数结束。

总结就是一句话当函数中有yield时，返回一个生成器对象，而不是一个值。当迭代该生成器对象时，函数中的代码会执行到yield处，然后返回yield后面的值，再次迭代时，会从yield处继续执行。

####### 利用生成器函数实现斐波那契数列
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(i for i in fibonacci(10))
```
    
##### 4. *号的使用
根据上下文的不同，其作用也不同。

###### 4.1 函数定义中的可变参数
```python
def foo(*args):
    print(args)

foo(1, 2, 3, 4, 5)

# 使用单个*号可以接收任意数量的位置参数，并将其放在一个元组中


def bar(**kwargs):
    print(kwargs)

# 使用双星号可以接收任意数量的关键字参数，并将其放在一个字典中

def foo(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)

print(1, 2, 3, 4, 5, m=6, n=7)
```


###### 4.2 函数调用时，参数解包
```python
# 单个*号可以将列表或元组解包为位置参数
def func(a, b, c):
    print(a, b, c)

args = [1, 2, 3]
func(*args)

# 双星号可以将字典解包为关键字参数
def func(a, b, c):
    print(a, b, c)


kwargs = {'a': 1, 'b': 2, 'c': 3}
func(**kwargs)
```

##### 4.3 用于列表，元组(tuple)的解构赋值
```python
# 星号可以用于解包列表或元组的剩余元素
first, *rest = [1, 2, 3, 4, 5]
print(first)  # 1
print(rest)  # [2, 3, 4, 5]
```

##### 5. 合并包
```python
# 合并包
a = [1, 2, 3]
b = [4, 5, 6]
c = [*a, *b]
print(c)

# result:
# [1, 2, 3, 4, 5, 6]
```

##### 6. 字典合并
```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
combined_dict = {**dict1, **dict2}
print(combined_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

##### 7. 强制关键字参数
```python
def func(a, b, *, c, d):
    print(a, b, c, d)

func(1, 2, c=3, d=4)

# 强制*后面的参数必须使用关键字参数传递
```

总结： 
根据不同的上下文，星号的作用也不同。
1）在函数定义中，星号可以用于接收任意数量的位置参数和关键字参数。
2）在函数调用时，星号可以用于解包列表、元组和字典。
3）在列表和元组的解构赋值中，星号可以用于解包剩余的元素。
