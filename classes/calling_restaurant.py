from restaurant  import Restaurant
restaurant_1=Restaurant('tary', 'kazakh')
print(f"The restaurant's name is {restaurant_1.restaurant_name}")
print(f"The cuisine is {restaurant_1.cuisine_type}")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()