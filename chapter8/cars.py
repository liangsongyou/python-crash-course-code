def make_car(manufacturer,model,**car_info):
    """
    Print information about the given car
    """
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    if car_info:
        for key,value in car_info.items():
            car[key] = value
    return car
           
print(make_car('subaru','outback',color='blue',year=2014))
print(make_car('audi','a1',convertible=False,color='blue',year=2012))