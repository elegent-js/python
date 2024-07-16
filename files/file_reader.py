from pathlib import Path

path = Path('files/pi_digits.txt')

contents = path.read_text()
lines = contents.splitlines()

for line in lines:
    print(line)