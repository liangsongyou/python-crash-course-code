#from car import Car,ElectricCar
# or we can do
import car
import electric_car

my_car = car.Car('audi','a4',2015)
your_car = electric_car.ElectricCar('tesla','model s',2016,70)

print('{}'.format(my_car.get_name()))   
print('{}'.format(your_car.get_name()))   
