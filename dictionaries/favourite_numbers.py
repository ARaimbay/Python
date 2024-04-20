favourite_numbers={
    'david' : [5, 9, 10],
    'aigerim' : [8, 7, 11],
    'lucy' : [45, 60],
    'caroline' : [67, 75],
    'fernando' : [34, 990]
}
for name, numbers in favourite_numbers.items():
    print(f"\n{name.title()}'s favourite numbers are:")
    for number in numbers:
        print(f"\t{number}")