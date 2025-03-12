from admin import User, Privileges, Admin

newAdmin = Admin('Bob', 'Dylan', 'BobbyDestroyer', 54)
newAdmin.describe_user()
newAdmin.privileges.show_privileges()
