class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(f"Restaurant's name is {self.restaurant_name} which has {self.cuisine_type} cuisine")
    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} is open.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors=['vanilla', 'strawberry', 'chocolate']
    def list_flavors(self):
        print(f"We have following tastes of ice-cream: {self.flavors}")


my_ice_cream=IceCreamStand('gelato place', 'italian')
print(my_ice_cream.describe_restaurant())
print(my_ice_cream.open_restaurant())
my_ice_cream.list_flavors()