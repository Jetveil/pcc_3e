current_users = ['s4s4l0', 'potter1337', 'waffle15', 'zasranpodshtan']
new_users = ['peppa17', 's4s4l0', 'waffle15', 'duremar']

for new_user in new_users:
    if new_user in current_users:  # Проверяем, есть ли имя в списке
        print(f'{new_user} is already used. Pick another name')
    else:
        print(f'{new_user} is available!')
