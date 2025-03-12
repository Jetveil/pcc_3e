from user import User


class Admin(User):
    def __init__(self, first_name, last_name, user_name, user_age):
        super().__init__(first_name, last_name, user_name, user_age)
        self.privileges = Privileges()


class Privileges():
    def __init__(self):
        self.privileges = ['ban users', 'delete users',
                           'add messages', 'edit messages']

    def show_privileges(self):
        print(f"Administrator privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
