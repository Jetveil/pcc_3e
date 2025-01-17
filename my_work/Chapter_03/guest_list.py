guest_list = ['Dude1', 'Dude2', 'Dude3']
print(guest_list)
print('------')

print(f'Guest {guest_list[1]} wont come')
print('------')

guest_list[1] = 'Waifu1'
print(f'{guest_list[1].title()} will come instead')
print('------')

print(f'Final guest list: {guest_list}')
print('------')

print(f'I invite you to the party, {guest_list[0]}')
print(f'I invite you to the party, {guest_list[1]}')
print(f'I invite you to the party, {guest_list[2]}')
print('------')

print('We bought a new larger table, so more guests can be invited')
print('-------')

guest_list.insert(0, 'Dude4')
guest_list.insert(2, 'Dude5')
guest_list.append('Dude6')

print(f'Final guest list is: {guest_list}')
print('-------')

print('Unfortunately only two gust can be invited')
print('-------')


print(f'Sorry, {guest_list.pop()} your invitation has expired')
print(f'Sorry, {guest_list.pop()} your invitation has expired')
print(f'Sorry, {guest_list.pop()} your invitation has expired')
print(f'Sorry, {guest_list.pop()} your invitation has expired')
print('-------')

print(f'{guest_list[0]}, you are still invited')
print(f'{guest_list[1]}, you are still invited')
print('-------')

del guest_list[0]
del guest_list[0]

print(guest_list)
