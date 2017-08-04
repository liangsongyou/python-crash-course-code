def city_country(city, country, population=None):
    """Return city,country neatly formatted."""
    if population:
        full = city + ', ' + country + ' - ' + 'population' + ' ' + str(population)
    else:
        full = city + ', ' + country
    return full.title()
