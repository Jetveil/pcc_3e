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

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# poll_ppl = ['jen', 'sarah', 'edward', 'phil', 'alina', 'mark']

# for name in poll_ppl:
#     if name in favorite_languages:
#         print(f"{name.title()}, thank you for taking the poll")
#     else:
#         print(f"{name.title()}, would you like to take a poll?")

# ex 6.7


# people = []

# person = {
#     'first_name': 'Semen',
#     'last_name': 'Swallow',
#     'age': 19,
#     'city': 'Kama'
# }
# people.append(person)

# person = {
#     'first_name': 'Ilya',
#     'last_name': 'Davydov',
#     'age': 30,
#     'city': 'Jopinsk'
# }
# people.append(person)

# person = {
#     'first_name': 'Gosha',
#     'last_name': 'Dudar',
#     'age': 24,
#     'city': 'Wonderland'
# }
# people.append(person)

# for person in people:
#     for k, v in person.items():
#         print(f"{k} : {v}")
#     print('----')

# ex 6.8


# pets = []

# pet = {
#     'nickname': 'markiz',
#     'animal': 'cat',
#     'owner': 'dim'
# }

# pets.append(pet)

# pet = {
#     'nickname': 'jessie',
#     'animal': 'dog',
#     'owner': 'sasha'
# }

# pets.append(pet)

# pet = {
#     'nickname': 'tori',
#     'animal': 'humster',
#     'owner': 'jack'
# }

# pets.append(pet)

# for pet in pets:
#     for k, v in pet.items():
#         print(f"{k.title()} : {v.title()}")
#     print('----')

# ex. 6.9

# favorite_places = {
#     'semen': ['grand canyon', 'alaska'],
#     'ilya davydov': ['hyperborea', 'atlantida', 'flander\'s house'],
#     'gosha dudar': ['infocygan valley']
# }

# for name, places in favorite_places.items():
#     print(f"{name.title()}\'s favorite places are:")
#     for place in places:
#         print(f"\t{place.title()}")

# ex 6.10

# favorite_numbers = {
#     'mandy': [42, 15, 228, 93],
#     'micah': [23, 0.1, 17],
#     'gus': [7, 12],
#     'hank': [1_000_000],
#     'maggie': [0],
# }

# for names, numbers in favorite_numbers.items():
#     print(f"{names.title()}\'s fav numbers are:")
#     for number in numbers:
#         print(f"\t{number}")

# ex. 6.11

# cities = {
#     'spb': {
#         'country': 'russia',
#         'population': '6 million',
#         'fact': 'moisty weather'
#     },
#     'beijing': {
#         'country': 'china',
#         'population': '22 million',
#         'fact': 'the longest street in the world'
#     },
#     'new york': {
#         'country': 'usa',
#         'population': '8.5 million',
#         'fact': 'the busiest railway station in the world'
#     }
# }

# cities['spb']['country'] = 'ukraine'

# for city, cityInfo in cities.items():
#     print(city.title())
#     for k, v in cityInfo.items():
#         print(f"\t{k.title()} : {v.title()}")
