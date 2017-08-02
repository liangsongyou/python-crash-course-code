file_path = './learning_python.txt'

with open(file_path) as file:
    lines = file.readlines()
    for line in lines:
        print(line.replace('Python','C'),end='')