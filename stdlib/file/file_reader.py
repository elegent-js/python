from pathlib import Path

path = Path('stdlib/file/pi_digits.txt')
content = path.read_text().rstrip()
print(content)

print()

contents = path.read_text().splitlines()
for line in contents:
    print(line)

print()
# 写入
path.write_text('3.1415926535\n8979323846\n2643383279\n5028841971\n6939937510\n5820974944\n5923078164\n0628620899\n8628034825\n3421170679\n')
content = path.read_text().rstrip()
print(content)



