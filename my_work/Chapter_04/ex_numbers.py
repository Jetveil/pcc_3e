for value in range(1, 21):
    print(value)

print('-----')

numbers = list(range(1, 1_000_001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

print('-----')

uneven_numbers = list(range(1, 21, 2))
for number in uneven_numbers:
    print(number)

print('-----')

multiple_of_three = list(range(3, 31, 3))
for number in multiple_of_three:
    print(number)

print('-----')

cubes = list(range(1, 11))
for num in cubes:
    num = num**3
    print(num)

print('-----')

cubes_generator = [value**3 for value in range(1, 11)]
print(cubes_generator)
