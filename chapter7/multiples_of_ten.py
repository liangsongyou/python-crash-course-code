number = input("Enter a number: ")

if number:
    number = int(number)
    if number % 10 == 0:
        print("{} is multiple of ten.".format(number))
    else:
        print("{} is not multiple of ten.".format(number))
else:
    print("Please provide a number next time.")