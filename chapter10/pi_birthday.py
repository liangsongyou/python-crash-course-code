file_name = './pi_million_digits.txt'

with open(file_name) as file:
    lines = file.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input('Enter your birthday, in the form mmddyy: ')
if birthday in pi_string:
    print('Your birthday appears in first million decimal digits of PI.')
else:
    print('You have a unique birthday.')