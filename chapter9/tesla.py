class Car():
    """Simple representation of a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_name(self):
        """Return a neatly formatted name."""
        name = str(self.year) + ' ' + self.make + ' ' + self.model
        return name.title()

    def read_odometer(self):
        """Return the current reading of odometer."""
        print('This car has run {} miles.'.format(self.odometer_reading))

    def update_odometer(self, miles):
        """Set the value of odometer to given value."""
        if miles > self.odometer_reading:
            self.odometer_reading = miles
        else:
            print('You can\'t roll back odometers.')

    def increment_odometer(self, miles):
        """Increment the odometer reading by miles."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print('You can\'t add negative value to odometer.')


class ElectricCar(Car):
    """Represent aspects of the car, specific to the electric car."""

    def __init__(self, make, model, year, battery=70):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = battery

    def describe_battery(self):
        """Describe the battery of electric car."""
        print('The car has {}-kWh battery.'.format(self.battery_size))

my_tesla = ElectricCar('tesla','model s',2017,80)
print('{}'.format(my_tesla.get_name()))
my_tesla.describe_battery()