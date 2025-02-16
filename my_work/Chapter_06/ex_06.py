# person = {
#     'first_name': 'Semen',
#     'last_name': 'Swallow',
#     'age': 19,
#     'city': 'Kama'
# }

# print(person['first_name'])
# print(person['last_name'])
# print(person['age'])
# print(person['city'])


# fav_nums = {
#     'Dude1': 12,
#     'Dude2': 15,
#     'Dude3': 1,
#     'Dude4': 100,
# }

# print(f'Dude1 favorite number is {fav_nums['Dude1']}')
# print(f'Dude2 favorite number is {fav_nums['Dude2']}')
# print(f'Dude3 favorite number is {fav_nums['Dude3']}')
# print(f'Dude4 favorite number is {fav_nums['Dude4']}')

# glossary = {
#     'Conditions': 'If Else statements',
#     'Lists': 'Changable sets of data []',
#     'Tuples': 'Unchangable sets of data ()"',
#     'Dictionaries': 'List of data with Key - Value format'
# }

# key = 'Conditions'
# print(f"{key} are : {glossary[key]}")
# key = 'Lists'
# print(f"{key} are : {glossary[key]}")
# key = 'Tuples'
# print(f"{key} are : {glossary[key]}")
# key = 'Dictionaries'
# print(f"{key} are : {glossary[key]}")

# ex 6.4

# glossary = {
#     'Conditions': 'If Else statements',
#     'Lists': 'Changable sets of data []',
#     'Tuples': 'Unchangable sets of data ()"',
#     'Dictionaries': 'List of data with Key - Value format',
#     '"keys()" method': 'loops throug dict. keys',
#     '"values()" method': 'loops throug dict. values',
#     '"items()" method': 'loops throug dict. key-val pairs'
# }

# for k, v in glossary.items():
#     if k.endswith('method'):
#         print(f"{k} is: {v}")
#     else:
#         print(f"{k} are: {v}")

# ex 6.5

# locations = {
#     'nile': 'egypt',
#     'volga': 'russia',
#     'yangtze': 'china'
# }

# for k, v in locations.items():
#     print(f"{k.title()} flows through {v.title()}")
# print('-----')
# for k in locations.keys():
#     print(f"{k.title()}")
# print('-----')
# for v in locations.values():
#     print(f"{v.title()}")

# ex 6.6

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

poll_ppl = ['jen', 'sarah', 'edward', 'phil', 'alina', 'mark']

for name in poll_ppl:
    if name in favorite_languages:
        print(f"{name.title()}, thank you for taking the poll")
    else:
        print(f"{name.title()}, would you like to take a poll?")
