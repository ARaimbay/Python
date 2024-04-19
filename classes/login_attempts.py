class User:
    def __init__(self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=0
    def describe_user(self):
        print(f"User's name is {self.first_name.title()} and last name is {self.last_name.title()}")
    def greet_user(self):
        print(f"Hello, {self.first_name.title()}!")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0


user_1=User('aigerim', 'raimbay')
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.reset_login_attempts()
print(user_1.login_attempts)