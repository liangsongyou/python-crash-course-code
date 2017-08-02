file_p = './guest_book.txt'

with open(file_p, 'a') as file:
    while True:
        name = input('What is your name? [q to quit]: ')
        if name == 'q':
            break
        else:
            file.write(name + '\n')
            file.write('[log] {} visited file.\n'.format(name))