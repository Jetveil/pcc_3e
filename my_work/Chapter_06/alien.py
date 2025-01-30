# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# alien_0['x_pos'] = 0
# alien_0['y_pos'] = -25
# print(alien_0)

# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)
# alien_0['color'] = 'red'
# alien_0['points'] = 15
# print(alien_0)

alien_0 = {'color': 'green', 'points': 5,
           'x_pos': 0, 'y_pos': 25, 'speed': 'fast'}
print(f'Original position: {alien_0["x_pos"]}')
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_pos'] += x_increment
print(f'New position with {alien_0["speed"]} speed: {alien_0["x_pos"]}')
