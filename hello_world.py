message = "hello python world!"
print(message)

message = "hello python crash course world!"
print(message)

# 单词首字母大写
print(message.title())

# 字符串中使用变量
first_name = "liu"
last_name = "peijun"
full_name = f'{first_name.title()}{last_name.title()}'
print(full_name)

print(" hello ".strip())

famous_person = "Albert Einstein"
message = f'{famous_person} once said, “A person who never made a mistake never tried anything new.”'
print(message)

print(2 ** 3)

print(0.1 + 0.2)

# 任意两个数相除的结果都是浮点数
print(4 / 2)

num = 1_000_000_000
print(num)

x, y, z = 0, 0, 0
print(f'{x}, {y}, {z}')

MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)

cars = ['bmw', 'audi', 'toyota', 'subaru', 'mercedes', 'volvo', 'ford', 'chevrolet', 'buick', 'cadillac', 'jeep', 'mazada']
print(cars)

### 排序
print(sorted(cars))

## 打印指定元素
print(cars[1])

## 取出最后的几个元素
print(cars[-1])
print(cars[-2])
print(cars[-3])

## replace
cars[0] = 'xiaomi'
print(cars)


## add at tail
cars.append('wenjie')
print(cars)

## insert at middle
cars.insert(1, 'h')
print(cars)

## delete
del cars[1]
print(cars)

# 删除末位元素，并持有
pop = cars.pop()
print(pop)

# 删除指定元素
cars.remove('audi')
print(cars)

# 按字母排序
cars.sort()
print(cars)

# 按字母排序，反向
cars.sort(reverse=True)
print(cars)

print(sorted(cars))
print(sorted(cars, reverse=True))

cars.reverse()
print(cars)

print(len(cars))
