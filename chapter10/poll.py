file_p = './poll.txt'

with open(file_p,'a') as file:
    print('Enter \'q\' to quit anytime.')
    while True:
        name = input('Name: ')
        if name == 'q':
            break
        file.write(name + '\'s message:\n')
        message = input('Why do you like programming? ')
        if message == 'q':
            break
        file.write(message + '\n')