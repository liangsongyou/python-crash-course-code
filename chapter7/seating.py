people = input("How many people are in the dinner group? ")

if people:
    people = int(people)
    if people > 8:
        print("You'll have to wait for a while.")
    else:
        print("Your table is ready all the time.")
else:
    print("Please provide number of people next time.:(")