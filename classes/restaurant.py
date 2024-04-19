class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(f"Restaurant's name is {self.restaurant_name} which has {self.cuisine_type} cuisine")
    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} is open.")


#restaurant_1=Restaurant('tary', 'kazakh')
#restaurant_2=Restaurant('dacha', 'ukranian')
#restaurant_3=Restaurant('bleur', 'french')

#print(f"The restaurant's name is {restaurant_1.restaurant_name}")
#print(f"The cuisine is {restaurant_1.cuisine_type}")
#restaurant_1.describe_restaurant()
#restaurant_1.open_restaurant()

#print(f"\nThe restaurant's name is {restaurant_2.restaurant_name}")
#print(f"The cuisine is {restaurant_1.cuisine_type}")
#restaurant_2.describe_restaurant()
#restaurant_2.open_restaurant()

#print(f"\nThe restaurant's name is {restaurant_3.restaurant_name}")
#print(f"The cuisine is {restaurant_3.cuisine_type}")
#restaurant_3.describe_restaurant()
#restaurant_3.open_restaurant()