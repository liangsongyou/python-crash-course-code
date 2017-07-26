favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# for name,language in favorite_languages.items():
#     print("{}'s favorite language is: {}.".format(name.title(),language.title()))

# for name in favorite_languages.keys():
#     print("{} Managed to take our poll. We thank you!".format(name.title()))

# friends = ['phil','sarah']

# for name in favorite_languages.keys():
#     print("{}".format(name.title()))
#     if name in friends:
#         print("Hi {}, I see your favorite language is {}".format(name.title(), favorite_languages[name].title()))

# if 'david' not in favorite_languages.keys():
#     print("David please take our poll.")

# for name in sorted(favorite_languages.keys()):
#     print("{}, thank you for taking our poll.".format(name.title()))

# print("The following languages have been mentioned:")
# for language in sorted(set(favorite_languages.values())):
#     print("{}".format(language.title()))

favorite_languages = {
    'jen': ['python','ruby'],
    'sarah': ['c'],
    'edward': ['ruby','go'],
    'phil': ['python','haskell'],
}

for name,languages in favorite_languages.items():
    if len(languages) < 2:
        print("{}'s favorite language is {}".format(name.title(),languages[0].title()))
    else:
        print("{}'s favorite languages are:".format(name.title()))
        for language in languages:
            print("\t{}".format(language.title()))
