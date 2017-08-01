"""A class to represent restuarants."""

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
