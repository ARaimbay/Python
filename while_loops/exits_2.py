prompt="\nPlease enter the pizza topping that you prefer to be added: "
prompt += "\n(Enter 'quit' when you are done.) "

while True:
    topping=input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"Your topping {topping} will be added to pizza")