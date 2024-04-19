def make_sandwich(*ingredients):
    print(f"\nMaking a sandwich with the following ingredients: ")
    for ingredient in ingredients:
        print(f"-{ingredient}")

make_sandwich('pickles', 'mushrooms', 'lettuce')