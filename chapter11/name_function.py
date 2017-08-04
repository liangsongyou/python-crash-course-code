def get_formatted_name(first, last, middle=None):
    """Generate a neatly formatted name."""
    if middle:
        name = first + ' ' + middle + ' ' + last
    else:
        name = first + ' ' + last
    return name.title()