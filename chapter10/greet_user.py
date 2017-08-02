import json

file_p = 'username.json'
with open(file_p) as file:
    username = json.load(file)
    print('Welcome back {}'.format(username))
    