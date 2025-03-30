from pathlib import Path
import json

# ex 10.1

# path = Path('my_work\Chapter_10\learning_python.txt')
# content = path.read_text(encoding='utf-8')
# lines = content.splitlines()
# for line in lines:
#     print(line)
#     print('--')

# print(content)


# ex 10.2

# path = Path('my_work\Chapter_10\learning_python.txt')
# content = path.read_text(encoding='utf-8')
# lines = content.splitlines()
# for line in lines:
#     line = line.replace('Python', 'C')  # <- Не забывать создавать переменную
#     print(line)


# ex 10.3

# path = Path('my_work\Chapter_10\learning_python.txt')
# content = path.read_text(encoding='utf-8')
# for line in content.splitlines():
#     line = line.replace('Python', 'C')  # <- Не забывать создавать переменную
#     print(line)


# ex 10.4

# path = Path('my_work\Chapter_10\guest.txt')
# guestName = input('Enter your name: ')

# path.write_text(guestName)

# ex 10.5

# path = Path('my_work\Chapter_10\guest_book.txt')

# namesList = []
# while True:
#     namePrompt = input("Enter user name: (or press Enter to quit)")
#     if namePrompt == "":
#         break
#     print(f"Hello, {namePrompt.title()}. We'll add you to the guest book")
#     namesList.append(namePrompt)

# file_string = ''
# for name in namesList:
#     file_string += f"{name.title()}\n"

# path.write_text(file_string)


# ex 10.6, 10.7

# print(f"Enter two values to sum or press Enter to quit")

# try:
#     firstVal = input(f"Enter first value: ")
#     if firstVal == "":
#         quit()
#     secondVal = input(f"Enter second value: ")
#     if firstVal == "":
#         quit()

# except ValueError:
#     print("Enter number, not text")
# else:
#     sum = int(firstVal) + int(secondVal)
#     print(f"The sum of {firstVal} and {secondVal} is: {sum}")


# 10.8

# filenames = ['cats.txt', 'dogs.txt']

# def read_files(filenames):
#     path = Path(f"my_work\Chapter_10\{filename}")
#     try:
#         contents = path.read_text()
#     except FileNotFoundError:
#         print(f"File {filename} not found")
#     else:
#         print(contents)

# for filename in filenames:
#     read_files(filenames)

# 10.9

# filenames = ['cats.txt', 'dogs.txt']

# def read_files(filenames):
#     path = Path(f"my_work\Chapter_10\{filename}")
#     try:
#         contents = path.read_text()
#     except FileNotFoundError:
#         pass
#     else:
#         print(contents)

# for filename in filenames:
#     read_files(filenames)


# 10.10

# file = Path("my_work\Chapter_10\pushkin.txt")
# text = file.read_text(encoding="UTF-8")
# repititions_count = text.count("но ")

# print(f"Повторений в тексте: {repititions_count}")


# 10.13


def get_stored_userInfo(path):
    """Получает хранимое имя пользователя, если оно существует."""
    if path.exists():
        contents = path.read_text()
        userInfo = json.loads(contents)
        return userInfo
    else:
        return None


def get_new_userInfo(path):
    """Запрашивает новое имя пользователя"""
    username = input("What's your name?: ")
    userAge = int(input("What's your age?: "))
    userCountry = input("What country were you born?: ")
    userInfo = {
        'username': username,
        'userAge': userAge,
        'userCountry': userCountry
    }
    contents = json.dumps(userInfo)
    path.write_text(contents)
    return userInfo


def greet_user():
    """Приветствует пользователя по имени"""
    path = Path('my_work\Chapter_10/users.json')

    userInfo = get_stored_userInfo(path)

    isNameCorrect = input(f"Is name {userInfo['username']} correct?")

    if userInfo:
        print(
            f"Welcome back, {userInfo['username']}, {userInfo['userAge']} years old from {userInfo['userCountry']}!")
    else:
        userInfo = get_new_userInfo(path)
        print(
            f"We will remember your name when you come back, {userInfo['username']}, {userInfo['userAge']} years old from {userInfo['userCountry']}")


greet_user()
