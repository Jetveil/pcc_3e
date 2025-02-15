favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

friends = ['phil', 'jen', 'semen']


# lang = favorite_languages['sarah'].title()

# print(f'Sarah\'s favorite language is {lang}')
# print('----')

# for name, lang in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {lang.title()}")

# print('----')

# for name in favorite_languages.keys():
#     print(name.title())

# print('---or---')

# for name in favorite_languages:
#     print(name.title())

# for name in favorite_languages.keys():
#     print(f"Hi, {name.title()}")
#     if name in friends:
#         lang = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see your fav language is {lang}")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for your poll")

print('-----')

print('These languages have been mentioned:')
for lang in favorite_languages.values():
    print(lang)

print('-----')

for lang in set(favorite_languages.values()):
    print(lang)

nums = {1, 2, 3, 4, 2, 1, 5}
print(nums)
