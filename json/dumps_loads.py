from pathlib import Path

import json

# Create a dictionary
numbers = [1, 2, 3, 4, 5]
contents = json.dumps(numbers)

print(contents)


path = Path("json/numbers.json")
contents = path.read_text()

numbers = json.loads(contents)
print(numbers[1])

