number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("{} is even.".format(number))
else:
    print("{} is odd".format(number))