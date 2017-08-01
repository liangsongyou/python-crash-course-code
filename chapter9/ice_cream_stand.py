class Restuarant():
    """A very basic representation of a restuarant."""

    def __init__(self, name, cuisine):
        """Initialize the restuarant's attributes."""
        self.name = name
        self.cuisine = cuisine

    def describe_restuarant(self):
        """Describe the restuarant."""
        print("{} offers {}.".format(self.name.title(),self.cuisine.title()))

    def open_restuarant(self):
        """Tell whether the restuarant is open or not."""
        print("{} is open now. You can get food here.".format(self.name.title()))

class IceCreamStand(Restuarant):
    """Describe an ice cream stand which is a special kind of restuarant."""

    def __init__(self, name, cuisine, flavors):
        """Initialize the restuarant's attributes."""
        super().__init__(name, cuisine)
        self.flavors = flavors

    def get_flavors(self):
        """Pretty print the flavors this ice cream stand offers."""
        if self.flavors:
            print('{} offers the following flavors.'.format(self.name.title()))
            for flavor in self.flavors:
                print('- {}'.format(flavor.title()))
        else:
            print('{} didn\'t tell what flavors they offer.'.format(self.name.title()))

std = IceCreamStand('bell ice creams','ice cream', ['chocolate','mango','strawberry'])

std.describe_restuarant()
std.open_restuarant()
std.get_flavors()