def get_formatted_name(first,last,middle=None):
    """Return a user's full name, nicely formatted."""
    if not middle:
        full = first + ' ' + last
    else:
        full = first + ' ' + middle + ' ' + last
    return full.title()

first = input('First Name: ')
last = input('Last Name: ')
mid = input('Do you have a middle name: [y/n] ')
if mid == 'y':
    middle = input('Middle Name: ')
    print('{}'.format(get_formatted_name(first,last,middle)))
else:
    print('{}'.format(get_formatted_name(first,last)))
