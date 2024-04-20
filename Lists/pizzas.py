pizzas=['four cheese', 'margarita', 'spicy chicken']
for pizza in pizzas:
    print(f'The best pizza ever is {pizza.title()}!')
print('\nI really love pizza!\n')

#make friend pizza equal to pizza
friend_pizzas=pizzas[:]
pizzas.append('coppenhagen pizza')
friend_pizzas.append('new york pizza')
print("My favourite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favourite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)