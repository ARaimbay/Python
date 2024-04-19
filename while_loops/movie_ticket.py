age=input("What is your age? ")
age=int(age)
if age < 3:
    print(f"\nThe ticket price for age of {age} is free")
if 3 < age < 12:
    print(f"\nThe ticket price for age of {age} is $10")
if  age >= 12:
    print(f"\nThe ticket price for age of {age} is $15")