# 演示将序列分解为单独的变量，即多变量赋值
p = (4, 5)
x, y = p

print(x)
print(y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data

print(name)
print(shares)
print(price)
print(date)

# 只要元素匹配，即可分解赋值，类似与ES6的解构赋值
name, shares, price, (year, mon, day) = data
print(name)
print(shares)
print(price)
print(year)
print(mon)
print(day)

# 不仅列表和元组可以分解，字符串，对象，迭代器等都可以分解
s = 'Hello'
a,b,c,d,e = s
print(a)
print(b)
print(c)
print(d)
print(e)

# 有时候只需要其中的某些值，可以使用占位符
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print(shares)
print(price)

