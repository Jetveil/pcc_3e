# --- Определение функции

# def greet_user():
#     """Greeting user"""  # Так называемая docstring - строка для документации
#     print("Hello")


# greet_user()
# help(greet_user)
# print(greet_user.__doc__)


# --- Передача значения (аргумента, аргумента) в функию

# def greet_user(username): # Аргумент функции
#     print(f"Hello, {username.title()}!")


# greet_user('Erma4ok') # Аргумент функции
# greet_user('Stru4ok') # Аргумент функции

# --- Позиционные аргументы

# def describe_pet(pet_type, pet_name):
#     print(f"I have a {pet_type} with the name of {pet_name.title()}.")


# describe_pet('cat', 'markiz')
# describe_pet('dog', 'buba')


# --- Именованные аргументы

# def describe_pet(pet_type, pet_name):
#     print(f"I have a {pet_type} with the name of {pet_name.title()}.")


# describe_pet(pet_type='cat', pet_name='markiz')


# --- Значения по умолчанию

# def describe_pet(pet_name, pet_type='cat'):
#     print(f"I have a {pet_type} with the name of {pet_name.title()}.")


# describe_pet(pet_name='markiz')
# describe_pet(pet_type='dog', pet_name='buba')


# --- Возвращаемое значение (return value)

# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()


# musician = get_formatted_name('jimi', 'hendrix')

# print(musician)

# --- Необязательные аргументы

# def get_formatted_name(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()


# dude = get_formatted_name('john', 'suckerman', 'bart')
# musician = get_formatted_name('michael', 'cocksun', 'lee')
# print(musician)
# print(dude)

# --- Возвращение словаря

def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}

    if 'age':
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)
