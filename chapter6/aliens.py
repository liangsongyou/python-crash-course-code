# alien_0 = {'color': 'green','points': 5}
# alien_1 = {'color': 'yellow','points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0,alien_1,alien_2]

# for alien in aliens:
#     print("{}".format(alien))

aliens = []

for alien in range(30):
    new_alien = {'color':'green','points':5,'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = fast

# showing first 5 aliens

for alien in aliens[:5]:
    print("{}".format(alien))

print("You'll have to deal with {} aliens.".format(len(aliens)))