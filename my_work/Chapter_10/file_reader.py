# from pathlib import Path

# path = Path('my_work/Chapter_10/pi_digits.txt')
# content = path.read_text().rstrip()

# print(content)


# --- Построчное считывание


# from pathlib import Path

# path = Path('my_work/Chapter_10/pi_digits.txt')
# content = path.read_text()

# lines = content.splitlines()
# for line in lines:
#     print(f"{line} <-")


# --- Работа с содержимым файла


from pathlib import Path

path = Path('solution_files\chapter_10\pi_million_digits.txt')
content = path.read_text()

lines = content.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string[:52])
print(len(pi_string))
