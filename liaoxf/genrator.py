# 演示generator
# 生成器
# 生成器是一个特殊的迭代器，可以通过函数生成

# 生成器的创建
g = (x * x for x in range(1_000_000_000))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print('-------------------')

for n in g:
    if (n < 1000):
        print(n)
    else:
        break

## 生成器函数
# 生成器函数是一个普通函数，只是在返回值时使用yield关键字
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'

f = fib(100)
for n in f:
    print(n)
