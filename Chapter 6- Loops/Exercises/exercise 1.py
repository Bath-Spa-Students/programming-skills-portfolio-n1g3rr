#Writing a loop
pizza_toppings = []

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ").lower()

    if topping == 'quit':
        break

    pizza_toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

print("\nYour pizza will have the following toppings:")
for topping in pizza_toppings:
    print("- " + topping)
