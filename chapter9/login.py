class User():
    """Describe a user of a service."""

    def __init__(self, first, last, username, email):
        """Initialize the attributes of user."""
        self.user = {}
        self.user['first'] = first
        self.user['last'] = last
        self.user['username'] = username
        self.user['email'] = email
        self.login_attempts = 0

    def describe_user(self):
        """Pretty print the user's info."""
        print("Here is {}'s info:".format(self.user['username']))
        for key,value in sorted(self.user.items()):
            print("{}: {}".format(key.title(),value))

    def greet_user(self):
        """Greet user formally."""
        print("Hi there, {}. Welcome to the site.".format((self.user['first'] + ' ' + self.user['last']).title()))

    def increment_login_attempts(self):
        """Increment the login attempts by user by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Set the login attempts back to 0."""
        self.login_attempts = 0

me = User('muhammad','ramzan','lightify','ramzanm461@gmail.com')
you = User('muhammad','ali','charlie','mali@mail.com')

me.describe_user()
you.describe_user()
me.increment_login_attempts()
print('{} tried to login {} times'.format(me.user['username'],me.login_attempts))
me.reset_login_attempts()
print('{} tried to login {} times'.format(me.user['username'],me.login_attempts))

