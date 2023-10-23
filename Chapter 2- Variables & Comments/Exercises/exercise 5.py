#Cost of each USB stick and the total budget
usb_stick_price = 6
total_budget = 50
# Calculate the number of USB sticks she can buy
num_usb_sticks = total_budget // usb_stick_price
# Calculate the remaining money
remaining_money = total_budget % usb_stick_price
# Display the results
print(f"She can buy {num_usb_sticks} USB sticks.")
print(f"She will have £{remaining_money} left.")