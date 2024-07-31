from pathlib import Path

import json

# Create a dictionary
numbers = [1, 2, 3, 4, 5]
contents = json.dumps(numbers)

print(contents)
print(type(contents))

path = Path("numbers.json")
contents = path.read_text()

numbers = json.loads(contents)
print(numbers[1])

