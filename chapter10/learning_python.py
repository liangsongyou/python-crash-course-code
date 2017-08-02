file_path = './learning_python.txt'

with open(file_path) as file:
    # printing entire file at once
    text = file.read()
    print(text)
    # looping through the file
    for content in file:
        print(content)
    # making list of file lines
    lines = file.readlines()

for line in lines:
   print(line)
    

