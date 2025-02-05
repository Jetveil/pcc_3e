person = {
    'first_name': 'Semen',
    'last_name': 'Swallow',
    'age': 19,
    'city': 'Kama'
}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])


fav_nums = {
    'Dude1': 12,
    'Dude2': 15,
    'Dude3': 1,
    'Dude4': 100,
}

print(f'Dude1 favorite number is {fav_nums['Dude1']}')
print(f'Dude2 favorite number is {fav_nums['Dude2']}')
print(f'Dude3 favorite number is {fav_nums['Dude3']}')
print(f'Dude4 favorite number is {fav_nums['Dude4']}')

glossary = {
    'Conditions': 'If Else statements',
    'Lists': 'Changable sets of data []',
    'Tuples': 'Unchangable sets of data ()"',
    'Dictionaries': 'List of data with Key - Value format'
}

key = 'Conditions'
print(f"{key} are : {glossary[key]}")
key = 'Lists'
print(f"{key} are : {glossary[key]}")
key = 'Tuples'
print(f"{key} are : {glossary[key]}")
key = 'Dictionaries'
print(f"{key} are : {glossary[key]}")
