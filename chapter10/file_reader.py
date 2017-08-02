file_path = '/home/friday/code/my/PCS/chapter10/digits.txt'

with open(file_path) as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())    