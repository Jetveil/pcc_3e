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

path = Path('my_work\Chapter_10\guest_book.txt')
