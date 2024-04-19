sandwich_orders=['pastrami', 'egg', 'pastrami', 'tuna', 'cheese', 'pastrami']
print("Deli has run out of pastrami sandwich\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
finished_sandwiches=[]
while sandwich_orders:
    order=sandwich_orders.pop()
    print(f"I made your {order.title()} sandwich")
    finished_sandwiches.append(order)
print("\nThe following sandwiches were ordered:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())