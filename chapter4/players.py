players = ['charles','martina','michael','florence','eli']
print("{}".format(players[0:3]))
print("{}".format(players[1:4]))
print("{}".format(players[:4]))
print("{}".format(players[2:]))
print("{}".format(players[-3:]))
# looping through a subset of list
print("Here are the first three players in my team:")
for player in players[:3]:
    print("{}".format(player.title()),end=' ')
