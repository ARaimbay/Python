prompt="\nTell me what pizza topping whould you like to add? "
prompt += "\(Enter 'quit' when you are finished.) "

message=""
while message != 'quit':
    message=input(prompt)
    if message != 'quit':
        print(f"Topping {message} will be added to pizza.")