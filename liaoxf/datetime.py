# 演示datetime内置模块

from datetime import datetime
now = datetime.now()
print(now)

dt = datetime(2015, 4, 19, 12, 20, 20)
print(dt)

print(dt.timestamp())
print(datetime.fromtimestamp(dt.timestamp()))
print(datetime.utcfromtimestamp(dt.timestamp()))

