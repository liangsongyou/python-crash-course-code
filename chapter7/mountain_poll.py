responses = {}

# set flag to indicate that polling is active
polling_active = True

while polling_active:
    # prompt for user's name
    name = input("What is your name? ")
    # prompt for user's response
    response = input("Which mountain would you like to climb someday? ")

    # store the response in dictionry
    responses[name] = response

    repeat = input("Would you like to let another person respond? [y/n] ")
    if repeat != 'y':
        polling_active = False


print("\n----Poll Results----\n")
for name,response in responses.items():
    print("{} would like to climb {}.\n".format(name.title(),response.title()))