favorite_places = {
    'david' :{
        'places' : ['rome','cambridge','new haven'],
    },
    'kareem': {
        'places': ['minsk','moscow','san jose'],
    },
    'andi': {
        'places': ['sacramento','vermont','richmond'],
    },
}

for person,favorite in favorite_places.items():
    print("{} likes to visit:".format(person.title()))
    for place in favorite['places']:
        print("\t{}".format(place.title()))