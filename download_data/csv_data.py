# 演示解析CSV文件

from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/weather.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

print([{"index": index, "header": header} for index, header in enumerate(header_row)])

dates, highs = [], []

for row in reader:
    dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
    highs.append(int(row[4]))

print("*" * 50)
print(dates)
print(highs)

# 根据最高温度绘图
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')

# 设置图形的格式
ax.set_title("Daily high temperatures, Jan 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
