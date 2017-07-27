
while True:
    age = input('Enter your age: ')
    age = int(age)
    if age <= 3:
        print('Your ticked is free.')
    elif age > 3 and age <= 12:
        print('Your ticket costs $10.')
    elif age > 12 and age < 100:
        print('Your ticket costs $15.')
    else:
        break