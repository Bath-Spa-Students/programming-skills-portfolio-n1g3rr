#dictionaries
pet1 = {'kind': 'dog', 'owner': 'Bilal'}
pet2 = {'kind': 'cat', 'owner': 'Fieezan'}
pet3 = {'kind': 'parrot', 'owner': 'Charlie'}

pets = [pet1, pet2, pet3]

for pet in pets:
    kind = pet['kind']
    owner = pet['owner']
    print(f"The {kind} is owned by {owner}.")
