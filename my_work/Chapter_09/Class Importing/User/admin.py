import privileges as pv

newAdmin = pv.Admin('Bobby', 'Sucker', 'FullMoon', 24)
newAdmin.describe_user()
newAdmin.greet_user()
newAdmin.privileges.show_privileges()
