guest_names=["fatima", "Bilal" , "Lahore the Pawa"]
for guest_name in guest_names:
 print(f"Dear {guest_name} , I would like to invite you to a dinner with me where I would like to ask you some important questions.")
 #space
guests_who_did_not_make_it="Lahore the Pawa"
print(f"\nUnfortunately, {guests_who_did_not_make_it} can't make it to dinner.")
#space
new_guest="Hakim Sahab"
guest_names[guest_names.index(guests_who_did_not_make_it)] = new_guest
for guest_name in guest_names:
 print(f"Dear {guest_name} , I would like to invite you to a dinner with me where I would like to ask you some important questions today at 7pm at pera hotel New York.")