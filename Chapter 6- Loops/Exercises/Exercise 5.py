# A list of called sanwiche orders
sandwich_orders = ['ham and cheese', 'turkey', 'pastrami', 'BLT', 'tuna', 'pastrami', 'vegetarian', 'pastrami']

finished_sandwiches = []

print("Sorry, the deli has run out of pastrami.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_order = sandwich_orders.pop(0)
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
