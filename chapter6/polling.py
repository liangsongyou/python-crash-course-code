favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

suggested = ['harvey','david','sarah','zed']

for person in suggested:
    if person in favorite_languages.keys():
        print("Thanks for your response, {}.".format(person.title()))
    else:
        print("Please help us by taking the poll, {}.".format(person.title()))