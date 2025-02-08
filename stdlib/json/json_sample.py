from pathlib import Path
import json

numbers = [1, 2, 3, 4, 5]
path = Path("stdlib/json/numbers.json")
contents = json.dumps(numbers)
path.write_text(contents)

print(path.read_text())

print('---------------------------------')

contents = json.loads(path.read_text())
print(contents)
