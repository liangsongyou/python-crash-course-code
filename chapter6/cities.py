cities = {
    'san jose': {
        'country' : 'united states',
        'population': '9393949',
        'fact': 'The tech hub of United States.',
    },
    'beijing': {
        'country': 'china',
        'population': '839394883',
        'fact': 'The capital of China.',
    },
    'tokyo': {
        'country': 'japan',
        'population': '32874834',
        'fact': 'The busiest city in the world.',
    },
}

for city,info in cities.items():
    print("We have some interesting facts about {}:".format(city.title()))
    print("{} is in {}".format(city.title(),info['country']))
    print("{} have {} people.".format(city.title(),info['population']))
    print("Fact: {}\n".format(info['fact']))
