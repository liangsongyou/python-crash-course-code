pets = ['dog','cat','dog','goldfish','cat','rabiit','cat']
print(pets)

not_needed = 'cat'

while not_needed in pets:
    pets.remove(not_needed)

print("{} was not needed so we removed it.".format(not_needed))
print(pets)