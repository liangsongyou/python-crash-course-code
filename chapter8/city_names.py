def city_country(city,country):
    """Return the name of city and country formatted"""
    return "{}, {}".format(city.title(), country.title())

france = city_country('paris','france')
germany = city_country('berlin','germany')
india = city_country('bengaluru','india')

print("{}".format(france))
print("{}".format(germany))
print("{}".format(india))