# --- counting.py

# current_number = 1

# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# --- quit.py

# prompt = "Enter something and I will write it back: "
# prompt += "\nIf you want to stop, type 'quit' "

# message = ""

# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# --- flags.py

# prompt = "Enter something and I will write it back: "
# prompt += "\nIf you want to stop, type 'quit' "

# active = True
# message = ""

# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# --- break

# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "

# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"You want to visit {city}")

# --- continue

# current_number = 0

# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     else:
#         print(current_number)

# --- confirmed_users --- WHILE ДЛЯ ПЕРЕБОРА СПИСКА

# unconfirmed_users = ['dude1', 'dude2', 'dude3']
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f"Verifying {current_user}")
#     confirmed_users.append(current_user)


# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(f"{confirmed_user}")

# --- pets --- WHILE ДЛЯ УДАЛЕНИЯ ОДИНАКОВЫХ ЗНАЧЕНИЙ ИЗ СПИСКА

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)

# --- СОХРАНЕНИЕ ВВЕДЕННОЙ ИНФОРМАЦИИ В СЛОВАРЕ

responses = {}

poll_isActive = True

while poll_isActive:
    name = input("\nName: ")
    response = input("\nMountain to visit: ")

    responses[name] = response

    repeat = input("\nAnother name? (yes/no) ")

    if repeat == 'no':
        poll_isActive = False

print('\nSummary: ')

for name, response in responses.items():
    print(f"{name.title()} whants to vsit {response.title()}")
