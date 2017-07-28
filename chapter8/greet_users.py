def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        print("Hello, {}".format(name.title()))

usernames = ['david','lauren','rob','zamyla']
greet_users(usernames)