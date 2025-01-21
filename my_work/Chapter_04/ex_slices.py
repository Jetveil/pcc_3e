names = ['karina', 'alina', 'alexandra', 'viktoria', 'arino4ka']
print('The first three names are:')
for name in names[:3]:
    print(name.title())

print('----')

print('Three names in the middle of the list are:')
for name in names[1:4]:
    print(name.title())

print('----')

print('Three names last names in the list are:')
for name in names[-3:]:
    print(name.title())
