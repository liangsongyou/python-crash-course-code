person_0 = {
    'first_name': 'muhammad',
    'last_name': 'ali',
    'age': 20,
    'city': 'islamabad',
}
person_1 = {
    'first_name': 'david',
    'last_name': 'malan',
    'age': 48,
    'city': 'cambridge',
}

person_2 = {
    'first_name': 'kareem',
    'last_name': 'zidane',
    'age': 26,
    'city': 'cairo',
}

people = [person_0,person_1,person_2]

print("We have record of {} people.\n".format(len(people)))
for person in people:
    print("First Name: {}".format(person['first_name'].title()))
    print("Last Name: {}".format(person['last_name'].title()))
    print("Age: {}".format(person['age']))
    print("Location: {}\n".format(person['city'].title()))
    
    