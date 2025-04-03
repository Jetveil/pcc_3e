from name_function import get_formatted_name

while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("\nPlese give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name is {formatted_name}")
