from pathlib import Path

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


print('\nEnter two numbers to divide (or "q" to quit)')

while True:
    first_num = input('\nEnter first number: ')
    if first_num == 'q':
        break

    second_num = input('Enter second number:')
    if second_num == 'q':
        break

    answer = int(first_num) / int(second_num)
    print(answer)
