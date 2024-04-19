class User:
    def __init__(self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name
    def describe_user(self):
        print(f"User's name is {self.first_name.title()} and last name is {self.last_name.title()}")
    def greet_user(self):
        print(f"Hello, {self.first_name.title()}!")

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.priviliges=['can add post', 'can delete post', 'can ban user']
    def show_priviliges(self):
        print(f"Administrator's priviliges are: {self.priviliges}")

#admin=Admin('aigerim', 'raimbay')
#print(admin.show_priviliges())