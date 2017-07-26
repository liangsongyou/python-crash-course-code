merk = {
    'name': 'merk',
    'kind': 'cat',
    'owner': 'mike',
}

beast = {
    'name': 'beast',
    'kind': 'dog',
    'owner': 'mark',
}

casper = {
    'name': 'casper',
    'kind': 'bull',
    'owner': 'smith',
}

pets = [merk, beast, casper]

print("We have following pets available:")
for pet in pets:
    print("Name : {}".format(pet['name'].title()))
    print("Kind : {}".format(pet['kind'].title()))
    print("Owner : {}\n".format(pet['owner'].title()))
    