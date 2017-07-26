users = {
    'aeinstien':{
        'first': 'albert',
        'last': 'einstien',
        'location': 'princeton',
    },
    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for user_name,user_info in users.items():
    print("Username: {}".format(user_name))
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: {}".format(full_name.title()))
    print("\tLocation: {}".format(location.title()))

