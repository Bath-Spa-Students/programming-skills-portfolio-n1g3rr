#  the loop
while True:
    # make the user to enter the age
    age_str = input("Please enter your age (type 'quit' to exit): ")

    
    if age_str.lower() == 'quit':
        break

    # converting age to an intiger
    try:
        age = int(age_str)

        
        if age < 3:
            ticket_cost = 0
        elif 3 <= age <= 12:
            ticket_cost = 10
        else:
            ticket_cost = 15

        
        print(f"The cost of your movie ticket is ${ticket_cost}.\n")

    except ValueError:
        print("Please enter a valid age or type 'quit' to exit.\n")
