# Start with your program from Exercise 3-5
guests = ["fatima", "fieezan", "Charlie", "David", "Eve"]

# Print a message saying you can invite only two people for dinner
print("Unfortunately, the new dinner table won't arrive in time. You can invite only two people for dinner.")

# Use pop() to remove guests from your list one at a time until only two names remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

# Print a message to each of the two people still on your list
for remaining_guest in guests:
    print(f"{remaining_guest}, you're still invited to dinner.")

# Use del to remove the last two names from your list
del guests[:]

# Print your list to make sure it's empty at the end of your program
print("Guest list:", guests)
