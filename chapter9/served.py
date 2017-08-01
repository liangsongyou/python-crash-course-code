class Restuarant():
    """A very basic representation of a restuarant."""

    def __init__(self, name, cuisine):
        """Initialize the restuarant's attributes."""
        self.name = name
        self.cuisine = cuisine
        self.served = 0

    def describe_restuarant(self):
        """Describe the restuarant."""
        print('{} offers {}.'.format(self.name.title(),self.cuisine.title()))

    def open_restuarant(self):
        """Tell whether the restuarant is open or not."""
        print('{} is open now. You can get food here.'.format(self.name.title()))

    def set_served(self, guests):
        """Set the value of served users to guests."""
        if guests >= 0:
            self.served = guests
        else:
            print('You can\'t serve negative guests.')

    def increment_served(self, guests):
        """Increment the number of guests served tot guests."""
        if guests >= 0:
            self.served += guests
        else:
            print('You can\'t add negative users.')

rest = Restuarant('la feth','french')
rest.set_served(300)
print('{} have served {} guests.'.format(rest.name.title(),rest.served))
rest.increment_served(-33)