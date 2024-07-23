# 演示*号关键字在Python中的作用

# 1. 用于函数定义时，收集多余的位置参数
def sum(*args):
    print(args)


# (1, 2, 3, 4, 5)
sum(1, 2, 3, 4, 5)


# 2. **kwargs用于函数定义时，收集参数组成字典
def print_kwargs(**kwargs):
    print(kwargs)


# {'name': 'Tom', 'age': 18}
print_kwargs(name='Tom', age=18)


# 3. 用于函数调用时，将列表或元组拆分为位置参数
# 单个*号可以将列表或元组解包为位置参数
def func(a, b, c):
    print(a, b, c)


args = [1, 2, 3]
func(*args)


# 4. 用于函数调用时，将字典拆分为关键字参数
# 两个*号可以将字典解包为关键字参数
def func(a, b, c):
    print(a, b, c)


kwargs = {'a': 1, 'b': 2, 'c': 3}
func(**kwargs)