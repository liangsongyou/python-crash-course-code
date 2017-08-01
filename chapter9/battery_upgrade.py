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

    def fill_gas_tank(self):
        """Simulate filling of gas tank of the car."""
        print('Filling gas tank of {}'.format(self.get_name()))


class Battery():
    """Describe a battery."""

    def __init__(self, battery_size):
        """Initialize attributes of battery."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Describe the battery of electric car."""
        print('The car has {}-kWh battery.'.format(self.battery_size))

    def get_range(self):
        range = None
        """Print the range the battery provides."""
        if self.battery_size == 70:
            range = 250
        if self.battery_size == 85:
            range = 310

        message = 'The Car can go approximately ' + str(range) + ' miles on full charge.'
        print('{}'.format(message))

    def upgrade_battery(self):
        """Upgrade the battery if not already upgraded."""
        if self.battery_size < 85:
            self.battery_size = 85        
        

class ElectricCar(Car):
    """Represent aspects of the car, specific to the electric car."""

    def __init__(self, make, model, year, battery_size=70):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery(battery_size)

    def fill_gas_tank(self):
        """Overriding the method from parent class. Since electric cars don't have gas tanks."""
        print('Electric cars don\'t even need a gas tank')


my_tesla = ElectricCar('tesla','model s',2017,70)
print('{}'.format(my_tesla.get_name()))
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()