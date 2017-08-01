"""A class to represent users of a service."""
class User():
    """Describe a user of a service."""

    def __init__(self, first, last, username, email):
        """Initialize the attributes of user."""
        self.user = {}
        self.user['first'] = first
        self.user['last'] = last
        self.user['username'] = username
        self.user['email'] = email

    def describe_user(self):
        """Pretty print the user's info."""
        print("Here is {}'s info:".format(self.user['username']))
        for key,value in sorted(self.user.items()):
            print("{}: {}".format(key.title(),value))

    def greet_user(self):
        """Greet user formally."""
        print("Hi there, {}. Welcome to the site.".format((self.user['first'] + ' ' + self.user['last']).title()))
