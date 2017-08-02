import json

file_p = 'numbers.json'

with open(file_p) as file:
    numbers = json.load(file)

print(numbers)