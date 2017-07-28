def get_formatted_name(first,last,middle=None):
    """Return a user's full name, nicely formatted."""
    if not middle:
        full = first + ' ' + last
    else:
        full = first + ' ' + middle + ' ' + last
    return full.title()

musician = get_formatted_name('chris','clan','john')
print("{}".format(musician))