prompt="\nPlease enter the pizza topping that you prefer to be added: "
prompt += "\n(Enter 'quit' when you are done.) "

active = True
while active:
    message=input(prompt)
    if message == 'quit':
        active=False
    else:
        print(f"Your topping {message} will be added to pizza")