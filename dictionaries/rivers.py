rivers_list={
    'nile' : 'egypt',
    'niva' : 'russia',
    'missisipi' : 'united states of america',
}
for river, country in rivers_list.items():
    print(f"\tThe {river.title()} runs through {country.title()}.")

for river in rivers_list.keys():
    print(river.title())

for country in rivers_list.values():
    print(country.title())