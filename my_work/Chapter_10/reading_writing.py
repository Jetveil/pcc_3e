from pathlib import Path
import json

# path = Path('chapter_10/reading_from_a_file/pi_million_digits.txt')
# content = path.read_text()

# lines = content.splitlines()

# pi_string = ''
# for line in lines:
#     pi_string += line.lstrip()

# birthday = input("Enter your BD in ddmmyy format:")
# if birthday in pi_string:
#     print("Your birthday is in first million digits of pi!")
# else:
#     print("Your birthday is not in first million digits of pi!")


# --- Запись одной строки

# path = Path('my_work/chapter_10/programming.txt')
# path.write_text('I love cocksucking!')


# --- Запись нескольких строк

# path = Path('my_work/chapter_10/programming_write.txt')

# contents = 'I love sucking\n'
# contents += 'I love fucking\n'
# contents += 'I love shitting\n'

# path.write_text(contents)


# --- Использование исключений для предотвращения
# аварийного завершения программы


# print('\nEnter two numbers to divide (or "q" to quit)')

# while True:
#     first_num = input('\nEnter first number: ')
#     if first_num == 'q':
#         break

#     second_num = input('Enter second number:')
#     if second_num == 'q':
#         break
#     try:
#         answer = int(first_num) / int(second_num)
#     except ZeroDivisionError:
#         print("You can't divide by 0")
#     else:
#         print(answer)

# --- Обработка исключения FileNotFoundError

# path = Path('chapter_10/exceptions/alice.txt')
# try:
#     contents = path.read_text(encoding='utf-8')
# except FileNotFoundError:
#     print(f"File {path} does not exists")
# else:
#     words = contents.split()
#     num_words = len(words)
#     print(f"The file {path.name} has about {num_words} words.")


# --- Работа с несколькими файлами

# path = Path('chapter_10/exceptions/')
# filenames = ['alice.txt', 'siddhartha.txt',
#              'moby_dick.txt', 'little_women.txt']


# def count_words(filenames):
#     """Подсчитывает приблизительное количество слов в файле"""
#     try:
#         contents = path.read_text(encoding='utf-8')
#     except FileNotFoundError:
#         print(f"File {path.name} does not exist")
#     else:
#         words = contents.split()
#         num_words = len(words)
#         print(f"The file {path.name} has about {num_words} words.")


# for filename in filenames:
#     path = Path(f"chapter_10/exceptions/{filename}")
#     count_words(path)

# --- Ошибки без уведомления пользователя


# path = Path('chapter_10/exceptions/')
# filenames = ['alice.txt', 'siddhartha.txt',
#              'moby_dick.txt', 'little_women.txt']


# def count_words(filenames):
#     """Подсчитывает приблизительное количество слов в файле"""
#     try:
#         contents = path.read_text(encoding='utf-8')
#     except FileNotFoundError:
#         pass  # <-- Пользователь не видит никакого сообщения об ошибке
#     else:
#         words = contents.split()
#         num_words = len(words)
#         print(f"The file {path.name} has about {num_words} words.")


# for filename in filenames:
#     path = Path(f"chapter_10/exceptions/{filename}")
#     count_words(path)


# --- Сохранение данных JSON

# nums = [2, 3, 5, 7, 11, 13]

# path = Path('my_work\Chapter_10/numbers.json')
# contents = json.dumps(nums)
# path.write_text(contents)


# --- Чтение данных JSON

# path = Path('my_work\Chapter_10/numbers.json')
# contents = path.read_text()
# nums = json.loads(contents)

# print(nums)

# --- Сохранение пользовательских данных

# path = Path('my_work\Chapter_10/users.json')
# username = input("What's your name?: ")
# contents = json.dumps(username)
# path.write_text(contents)
# print(f"We will remember your name when you come back, {username}")


# --- Чтение пользовательских данных

# path = Path('my_work\Chapter_10/users.json')
# contents = path.read_text()
# username = json.loads(contents)

# print(f"Welcome, {username}!")

# --- Объединение записи и чтения в один файл

# path = Path('my_work\Chapter_10/users.json')
# if path.exists():
#     path = Path('my_work\Chapter_10/users.json')
#     contents = path.read_text()
#     username = json.loads(contents)
#     print(f"Welcome, {username}!")
# else:
#     username = input("What's your name?: ")
#     contents = json.dumps(username)
#     path.write_text(contents)
#     print(f"We will remember your name when you come back, {username}")


# --- Рефакторинг

# def get_stored_username(path):
#     """Получает хранимое имя пользователя, если оно существует."""
#     path = Path('my_work\Chapter_10/users.json')
#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         return username
#     else:
#         return None


# def get_new_username(path):
#     """Запрашивает новое имя пользователя"""
#     path = Path('my_work\Chapter_10/users.json')
#     username = input("What's your name?: ")
#     contents = json.dumps(username)
#     path.write_text(contents)
#     return username


# def greet_user():
#     """Приветствует пользователя по имени"""
#     path = Path('my_work\Chapter_10/users.json')
#     username = get_stored_username(path)
#     if username:
#         print(f"Welcome back, {username}!")
#     else:
#         username = get_new_username(path)
#         print(f"We will remember your name when you come back, {username}")


# greet_user()
