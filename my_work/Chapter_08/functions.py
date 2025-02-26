# --- Определение функции

def greet_user():
    """Greeting user"""  # Так называемая docstring - строка для документации
    print("Hello")


greet_user()
help(greet_user)
print(greet_user.__doc__)
