class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served = 5
    def describe_restaurant(self):
        print(f"Restaurant's name is {self.restaurant_name} which has {self.cuisine_type} cuisine")
    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} is open.")
    def set_number_served(self):
        print(f"This restaurant served {self.number_served} guests")
    def update_number_served(self, number):
        self.number_served = number
    def increment_number_served(self, number):
        self.number_served += number


restaurant=Restaurant('tary', 'kazakh')
restaurant.describe_restaurant()

restaurant.increment_number_served(10)
restaurant.set_number_served()