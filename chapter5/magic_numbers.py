import random

number = random.randint(1,100)
guess = int(input("Enter a number: "))

while True:
    if guess < number:
        print("Too Low.Guess Again:)")
        guess = int(input("[1-100]: "))
    elif guess > number:
        print("Too High.Guess Again:)")
        guess = int(input("[1-100]: "))
    else:
        print("Voila. You got.")
        break