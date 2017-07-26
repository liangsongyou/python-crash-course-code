rivers = {
    'nile': 'egypt',
    'ganges': 'india',
    'thames': 'england',
}

for river,country in sorted(rivers.items()):
    print("The {} runs through {}".format(river.title(),country.title()))

print("Following countries have been mentioned:")
for country in sorted(rivers.values()):
    print("{}".format(country.title()))
    
print("Following rivers have been mentioned:")
for river in sorted(rivers.keys()):
    print("{}".format(river.title()))