"""A set of classes to represent admin level users."""
from user import User

class Priviliges():
    """Describe privliges of a user."""

    def __init__(self, priviliges):
        """Initialize privliges for a user."""
        self.priviliges = priviliges


    def show_priviliges(self):
        """Pretty print the priviliges of the admin user."""
        if self.priviliges:
            print('The user have following priviliges:')
            for privilige in self.priviliges:
                print('- {}'.format(privilige.title()))
        else:
            print('The user have no priviliges')

class Admin(User):
    """Describe an admin i.e. a special kind of user."""

    def __init__(self, first, last, username, email, priviliges=None):
        """Initialize attributes for the admin user."""
        super().__init__(first, last, username, email)
        self.priviliges = Priviliges(priviliges)