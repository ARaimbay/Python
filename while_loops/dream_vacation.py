responses={}
polling_active=True
while polling_active:
    name=input("\nWhat is your name? ")
    response=input("If you could visit one place in the world, where would you go? ")
    responses[name]=response
    repeat=input("Would you like to let another place to record? (yes/no) ")
    if repeat == 'no':
        polling_active=False
print("\n---Poll Result ---")
for name, response in responses.items():
    print(f"{name.title()} dreams to have vacation at {response.title()}.")