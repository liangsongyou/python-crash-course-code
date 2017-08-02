import json

file_p = 'favorite.json'

with open(file_p,'w') as file:
    favorite = input('What is your favorite number? ')
    json.dump(favorite, file)
    