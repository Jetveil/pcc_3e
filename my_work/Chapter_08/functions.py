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

def describe_pet(pet_name, pet_type='cat'):
    print(f"I have a {pet_type} with the name of {pet_name.title()}.")


describe_pet(pet_name='markiz')
describe_pet(pet_type='dog', pet_name='buba')
