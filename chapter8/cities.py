def describe_city(name,country='united states'):
    """Describes the city"""
    print("{} is in {}".format(name.title(),country.title()))

describe_city('richmond')
describe_city('london','england')
describe_city('rome','italy')