class Dog():
    """Simple representation of a dog."""

    def __init__(self, name, age):
        """Set the properties of dog object."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a sitting dog."""
        print("{} is now sitting.".format(self.name.title()))

    def roll_over(self):
        """Simulate a roll over by dog."""
        print("{} just rolled over!".format(self.name.title()))

    def get_age(self):
        """Tell the age of dog."""
        print("{} is {} years old.".format(self.name.title(),self.age))


willie = Dog('willie',5)
print("My dog's name is {}".format(willie.name.title()))
willie.sit()
willie.roll_over()
willie.get_age()