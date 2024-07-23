# 数字的四舍五入
print(round(10.12623, 2))


# 执行精确的浮点数运算(科学计算，工程领域，金融领域)
from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
print(a + b)
print((a + b) == Decimal('6.3'))

# 数字的格式化输出
x = 1234.56789
# 保留两位小数
print(format(x, '0.2f'))

# 右对齐
print(format(x, '>10.1f'))

# 左对齐
print(format(x, '<10.1f'))

# center
print(format(x, '^10.1f'))

# 千位分隔符
print(format(x, ','))

# 千位分隔符，保留一位小数
print(format(x, '0,.1f'))

# 指数计数法
print(format(x, 'e'))

# 指数计数法，保留两位小数
print(format(x, '0.2e'))
