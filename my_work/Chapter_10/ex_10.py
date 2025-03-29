from pathlib import Path

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
