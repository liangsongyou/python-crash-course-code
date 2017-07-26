favorite_numbers = {
    'david': [3,6,11],
    'rob': [9],
    'tommy': [4,1,7],
    'vanessa': [11,1,4,8],
    'maria': [3,2,5],
}

for name,numbers in favorite_numbers.items():
    if len(numbers) < 2:
        print("\n{}'s favorite number is {}".format(name.title(),numbers[0]))
    else:
        print("\n{}'s favorite numbers are:".format(name.title()))
        for number in numbers:
            print("\t{} ".format(number),end='')