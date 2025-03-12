class User:
    def __init__(self, first_name, last_name, user_name, user_age):
        self.name = first_name.title()
        self.surname = last_name.title()
        self.username = user_name
        self.age = user_age

    def describe_user(self):
        print(f"\nUser name: {self.name}")
        print(f"User last name: {self.surname}")
        print(f"User nickname: {self.username}")
        print(f"User age: {self.age}")

    def greet_user(self):
        print(f"Hello, {self.name} {self.surname} as {self.username}")


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
