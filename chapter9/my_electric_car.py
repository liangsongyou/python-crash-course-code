from car import ElectricCar

my_tesla = ElectricCar('tesla','model s',2016, 70)

print('{}'.format(my_tesla.get_name()))
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()