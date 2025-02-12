favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

lang = favorite_languages['sarah'].title()

print(f'Sarah\'s favorite language is {lang}')
print('----')

for name, lang in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {lang.title()}")
