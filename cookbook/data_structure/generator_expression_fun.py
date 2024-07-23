# 演示生成器函数(一个使用yield关键字的函数)，生成器函数用来生成生成器

def simple_generator():
    for x in range(3):
        yield x

# 使用生成器函数
gen = simple_generator()
arr = [x for x in gen]
print(arr)


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
a = my_gen()
print(a)

# fibonnaci sample
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print([i for i in fibonacci(100)])