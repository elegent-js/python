# 基本日期与时间转换

# 表示时间段
from datetime import timedelta

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b

print(c.days)
print(c.seconds)
print(c.seconds / 3600)
print(c.total_seconds())


# 表示特定的日期和时间
from datetime import datetime


a = datetime(2012, 9, 23)
print(a)

b = datetime(2012, 12, 21)
d = b - a
print(d)

now = datetime.today()
print(now)

print(now + timedelta(minutes=10))


# 字符串转换为日期
from datetime import datetime
text = '2012-09-20 01:02:03'
y = datetime.strptime(text, '%Y-%m-%d %H:%M:%S')
print(y)