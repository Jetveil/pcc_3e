# Nesting (Вложенность)

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# ------

# aliens = []

# for alien_number in range(30):
#     new_alien = {'color': 'green', 'speed': 'slow', 'points': 5}
#     aliens.append(new_alien)

# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = '10'

# for alien in aliens[:5]:
#     print(alien)


# print(f"Total number of aliens: {len(aliens)}")

# ------

# fav_langs = {
#     'gosha': ['python', 'haskell'],
#     'sarah': ['c'],
#     'jen': ['python', 'rust'],
#     'edward': ['rust', 'go']
# }

# for name, languages in fav_langs.items():
#     if len(languages) > 1:
#         print(f"{name.title()}'s favorite languages are:")
#         for language in languages:
#             print(language.title())
#     else:
#         print(f"{name.title()}'s favorite language is:")
#         for language in languages:
#             print(language.title())

# --------

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, userinfo in users.items():
    print(f"Username: {username}")
    fullName = f"{userinfo['first']} {userinfo['last']}"
    location = f"{userinfo['location']}"
    print(f"\tFull name: {fullName.title()}")
    print(f"\tLocation: {location.title()}")
