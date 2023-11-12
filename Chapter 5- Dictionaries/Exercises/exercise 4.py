# directionasry
rivers_countries = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China'
}
print("Rivers and their countries:")
for river, country in rivers_countries.items():
    print(f"The {river} runs through {country}.")
#loop used to print 
print("\nRivers:")
for river in rivers_countries.keys():
    print(river)
print("\nCountries:")
for country in rivers_countries.values():
    print(country)
