# Strings equality
car1 = 'bmw'
car2 = 'subaru'
print(car1 == car2)
print(car1 != car2)

print('----')

name1 = 'Semen'
name2 = 'semen'
print(name1 == name2)
print(name1.lower() == name2)

print('----')

a = 1
b = 3
c = 5
if a > b and c > b:
    print('False')
if a > b or c > b:
    print('True')
