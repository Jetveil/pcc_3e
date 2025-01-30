# users = ['david', 'sonne', 'admin', 'michael', 'alina']
# if not users:
#     print('Wee need to add some users.')
# for user in users:
#     if user == 'admin':
#         print('Hello, Admin. Do you want to look at status report?')
#     else:
#         print(f'Hello, {user.title()}. Thank you for logging in.')

# current_users = ['s4s4l0', 'potter1337', 'waffle15', 'zasranpodshtan']
# new_users = ['peppa17', 'S4s4l0', 'Waffle15', 'duremar']
# current_users_lower = [user.lower() for user in current_users]

# for new_user in new_users:
#     if new_user.lower() in current_users_lower:
#         print(f'{new_user} is already used. Pick another name')
#     else:
#         print(f'You can use {new_user} name')

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in nums:
    if num == 1:
        print(f'\n{num}st')
    elif num == 2:
        print(f'\n{num}nd')
    elif num == 3:
        print(f'\n{num}rd')
    else:
        print(f'\n{num}th')
