"""A set of classes describing electric cars."""
from car import Car

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
