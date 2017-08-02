file_p = './guest.txt'

with open(file_p, 'a') as file:
    name = input('What is your name? ')
    file.write(name + '\n')