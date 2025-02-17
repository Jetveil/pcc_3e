pizza = {
    'dough': 'thin',
    'toppings': ['pepperoni', 'mushrooms', 'extra cheese']
}

print(f"You ordered a {pizza['dough']
                       }-dough pizza with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
