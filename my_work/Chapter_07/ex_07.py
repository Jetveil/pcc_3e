# --- 7.1

# requestedCar = input("What car do you want to rent? ")
# print(requestedCar)

# --- 7.2

# seats_amount = input("How many seats do you want to book? ")
# seats_amount = int(seats_amount)

# if seats_amount > 8:
#     print("You want to book more than 8 seats, so you need to wait")
# else:
#     print("The table is reserved for you")

# --- 7.3

# num = input("Enter a number: ")
# num = int(num)

# if num % 10 == 0:
#     print(f"Number {num} is multiple of 10")
# else:
#     print(f"Number {num} is not multiple of 10")


# --- 7.4

# prompt = "\nEnter pizza topping: "

# while True:
#     topping = input(prompt)
#     if topping == 'quit':
#         break
#     else:
#         print(f"You added {topping}")

# --- 7.5

# prompt = "\nEnter your age: "
# prompt += "\nEnter 'quit' to exit "

# while True:
#     age = input(prompt)
#     if age == 'quit':
#         break
#     age = int(age)

#     if age < 3:
#         print("The ticket is free")
#     elif 3 <= age < 12:
#         print("The ticket is 10$")
#     else:
#         print("The ticket is 15$")

# --- grok

# Задача: "Калькулятор скидок в магазине"

# Напиши программу, которая:

#     Запрашивает у пользователя название товара (строка, string).
#     Запрашивает возраст покупателя (число, int).
#     Если пользователь вводит 'stop' вместо названия товара, программа завершает работу.
#     В зависимости от возраста определяет скидку:
#         До 18 лет — скидка 20%.
#         От 18 до 60 лет — скидка 10%.
#         Старше 60 лет — скидка 30%.
#     Выводит сообщение с названием товара и размером скидки.

# while True:
#     good = input("Enter the good's name (or 'stop' to exit): ")
#     if good == 'stop':
#         break
#     age = input("Enter your age: ")

#     try:
#         age = int(age)

#         if age < 18:
#             print(f"Your discount for {good} is 20%")
#         elif 18 <= age <= 60:
#             print(f"Your discount for {good} is 10%")
#         else:
#             print(f"Your discount for {good} is 30%")
#     except ValueError:
#         print("Please enter a valid age (a whole number)!")

# --- 7.8

# sandwich_orders = ['chill burger', 'chivito', 'doner kebab', 'gyro']
# finished_sandwiches = []

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"{current_sandwich.title()} is coocking!")
#     finished_sandwiches.append(current_sandwich)

# print("\nTotal sandwiches coocked:")

# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich.title())

# --- 7.9

# sandwich_orders = ['pastrami', 'chill burger', 'pastrami',
#                    'chivito', 'doner kebab', 'gyro', 'pastrami']
# finished_sandwiches = []
# print("We are out of pstrami")

# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     finished_sandwiches.append(current_sandwich)
#     print(f"Coocking {current_sandwich.title()}...")

# for finished_sandwich in finished_sandwiches:
#     print(f"{finished_sandwich} is done!")

# --- 7.10

# vacation_places = {}

# poll_IsActive = True

# while poll_IsActive:
#     name = input("Enter your name: ")
#     prompt = input("Where would you like to go on Earth?: ")

#     vacation_places[name] = prompt

#     repeat = input("Enter another name? (yes/no): ")

#     if repeat == 'no':
#         break
#     else:
#         continue

# for name, place in vacation_places.items():
#     print(f"{name.title()} wants to visit {place.title()} ")
