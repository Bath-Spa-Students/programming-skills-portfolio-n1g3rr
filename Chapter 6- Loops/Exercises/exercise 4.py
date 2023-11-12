#A list of called sandwiches
sandwich_orders = ['ham and cheese', 'turkey', 'BLT', 'tuna', 'vegetarian']

finished_sandwiches = []

#loop through the list of sanwiches ordered
while sandwich_orders:
    current_order = sandwich_orders.pop(0)
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
