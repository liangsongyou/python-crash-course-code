players = ['charles','martina','michael','florence','eli']
print("{}".format(players[0:3]))
print("{}".format(players[1:4]))
print("{}".format(players[:4]))
print("{}".format(players[2:]))
print("{}".format(players[-3:]))

# using a for loop to iterate through subset of list
print("The first three players in our team are:")
for player in players[:3]:
    print("{}".format(player))
