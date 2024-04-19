from user_module import User
class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.priviliges=['can add post', 'can delete post', 'can ban user']
    def show_priviliges(self):
        print(f"Administrator's priviliges are: {self.priviliges}")