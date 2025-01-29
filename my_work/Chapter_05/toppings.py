# requested_toppings = ['mushrooms', 'jalapeno']

# if 'mushrooms' in requested_toppings:
#     print('Adding mushrooms')
# if 'jalapeno' in requested_toppings:
#     print('Adding jalapeno')
# if 'pepperoni' in requested_toppings:
#     print('Adding pepperoni')


# requested_toppings = ['mushrooms', 'jalapeno', 'pepperoni']
# for topping in requested_toppings:
#     print(f'Adding {topping} to you pizza!')

requested_toppings = ['mushrooms', 'jalapeno', 'pepperoni']
for topping in requested_toppings:
    if topping == 'jalapeno':
        print('Sorry, we are out of jalapeno')
    else:
        print(f'Adding {topping} to you pizza!')
