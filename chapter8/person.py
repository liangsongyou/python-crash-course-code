def build_person(first,last,age=None):
    """Return a dictionary of information about a person"""
    person = { 'first': first, 'last': last}
    if age:
        person['age'] = age
    return person

def print_name(person):
    if person.__contains__('age'):
            first = person['first']
            last = person['last']
            age = person['age']
            print("Name: {}, Age: {}".format(first.title() + ' ' + last.title(), age))
        
musician = build_person('jimi','hendrix',27)
print_name(musician)