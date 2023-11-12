#In this instance, the application verifies the user's age and outputs the appropriate message based on the given age ranges. To observe how the program outputs different messages for different age groups, change the value of the age variable.
# Set a value for the variable age
age = 25

# If-elif-else chain to determine the person's stage of life
if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")
