prompt = '\nTell me something and I\'ll repeat it back to you'
prompt += '\nEnter quit to end the program: '

# while True:
#     message = input(prompt)
#     if message == 'quit' or message == 'Quit':
#         exit() # or break can be used
#     else:
#         print("{}".format(message))
            

# using flags to determine program running time

active = True
while active:
    message = input(prompt)
    if message.lower() == 'quit':
        active = False
    else:
        print("{}".format(message))