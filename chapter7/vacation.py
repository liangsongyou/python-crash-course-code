places = {}
poll_active = True

while poll_active:
    name = input("Enter your name: ")
    place = input("What is the place you would like to visit: ")

    places[name] = place
    choice = input("Would you like to continue? [y/n] ")
    if choice != 'y':
        break

print("\n--- Poll Results ---\n")
for name,place in places.items():
    print("{} would like to visit {}.\n".format(name.title(),place.title()))