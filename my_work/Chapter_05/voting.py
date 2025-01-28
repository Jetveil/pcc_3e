age = 19
if age >= 18:
    print('You old enogh to vote')
    print('Have you registered to vote?')
else:
    print('Sorry, you are too young to vote')

print('-----')

age_1 = 31

if age_1 < 4:
    print('Your admission cost is 0$')
elif age_1 < 18:
    print('Your admission cost is 25$')
else:
    print('Your admission cost is 40$')

print('-----')

age_2 = 17
if age_2 < 4:
    price = 0
elif age_2 < 18:
    price = 25
else:
    price = 40

print(f'Your admission cost is ${price}')

print('-----')

age_3 = 66
if age_3 < 4:
    price = 0
elif age_3 < 18:
    price = 25
elif age_3 < 65:
    price = 40
else:
    price = 20

print(f'Your admission cost is ${price}')
