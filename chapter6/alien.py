# alien_0 = {'color': 'green','points': 5}
# new_points = alien_0['points']
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25

# # print("Color: {}".format(alien_0['color']))
# # print("Points: {}".format(alien_0['points']))
# #print("You just earned {} points.".format(new_points))
# print("{}".format(alien_0))

alien_0 = {'x_position': 0,'y_position': 25,'speed': 'medium'}
print("Original X-Position: {}".format(alien_0['x_position']))

# Move the alien to the right
# Determine how far to move the alien based on its current speed

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] += x_increment

print("New X-Position: {}".format(alien_0['x_position']))

# deleting key from the dictionary

del alien_0['y_position']
print("{}".format(alien_0))