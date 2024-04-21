class Employee:
    def __init__(self, first_name, last_name, annual_salary, default_raise, custom_raise, annual_raise):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        self.default_raise = 5000
        self.custom_raise = custom_raise
        self.annual_raise = annual_raise
    def give_default_raise(self):
       if self.annual_raise == 0:
           self.annual_salary = self.annual_salary + self.default_raise
    def give_custom_raise(self):
        if self.annual_raise != 0:
            self.annual_salary = self.annual_salary + self.custom_raise