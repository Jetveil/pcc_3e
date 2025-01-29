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

# requested_toppings = ['mushrooms', 'jalapeno', 'pepperoni']
# if requested_toppings:
#     for topping in requested_toppings:
#         if topping == 'jalapeno':
#             print('Sorry, we are out of jalapeno')
#         else:
#             print(f'Adding {topping} to you pizza!')
# else:
#     print('Are you sure that you want a plain pizza?')

avaliable_toppings = ['mushrooms', 'jalapeno', 'pepperoni']
requested_toppings = ['mushrooms', 'ice cream', 'pepperoni']
for topping in requested_toppings:
    if topping in avaliable_toppings:
        print(f'Adding {topping} to your pizza')
    else:
        print(f'Sorry, we dont have {topping} topping')
