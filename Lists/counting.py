#odd numbers
numbers=range(1,20,2)
for number in numbers:
    print(number)

#for numbers from 3 to 30 multiples of 3
numbers=[number*3 for number in range(3,30)]
print(numbers)

#for numbers from 1 to 10 cubes of them
numbers=[number**3 for number in range(1,10)]
print(numbers)