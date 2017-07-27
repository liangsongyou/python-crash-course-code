name = input('Please enter your name: ')
print("Hello, {}".format(name.title()))

# storing prompt in a variable

prompt = 'If you tell us who you are, we can personalize the message you see.'
prompt += '\nWhat is your name? '

name = input(prompt)
print("Hello, {}".format(name.title()))