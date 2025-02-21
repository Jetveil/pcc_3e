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
