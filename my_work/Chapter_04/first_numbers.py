for value in range(1, 5):
    print(value)

print('-----')

for value in range(5):
    print(value)

print('-----')

numbers = list(range(0, 6))
print(numbers)

print('-----')

even_numbers = list(range(2, 11, 2))
print(even_numbers)

square_numbers = []
for value in range(1, 11):
    square = value**2
    square_numbers.append(square)
print(square_numbers)

print('-----')

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

print('-----')

squares = [value**3 for value in range(1, 11)]
print(squares)
