pizzas = ['Alfredo', 'Pepperoni', 'Roman']
friend_pizzas = pizzas[:]
pizzas.append('New Pizza')
friend_pizzas.append('New Friend\'s pizza')

print('My fav pizzas:')
for pizza in pizzas:
    print(pizza)

print('----')

print('My friend\'s fav pizzas:')
for pizza in friend_pizzas:
    print(pizza)
