def get_formatted_name(first, last):
    """Display a simple greeting"""
    full = first + ' ' + last
    return full.title()


while True:
    print("\nPlease tell me your name")
    print("Enter q anytime to quit.")
    first = input("First Name: ")
    if first == 'q':
        break

    last = input("Last Name: ")
    formatted = get_formatted_name(first, last)
    print("\n Hello, {}".format(formatted))
