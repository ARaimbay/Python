sandwich_orders=['chicken', 'egg', 'cheese']
finished_sandwiches=[]
while sandwich_orders:
    order=sandwich_orders.pop()
    print(f"I made your {order.title()} sandwich")
    finished_sandwiches.append(order)
print("\nThe following sandwiches were ordered:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())