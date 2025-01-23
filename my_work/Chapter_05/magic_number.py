answer = 17
if answer != 42:
    print('Not correct answer')

age_0 = 18
age_1 = 21

if (age_0 >= 17) and (age_1 >= 17):
    print('True')
else:
    print('False')

print('----')

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

banned_users = ['pshek', 'vova boba', 'leo']
user = 'dude'
if user not in banned_users:
    print(f'\n{user.title()} can whrite here')
else:
    print(f'\n{user.title()} can not whrite here')


game_active = True
can_whrite = False
