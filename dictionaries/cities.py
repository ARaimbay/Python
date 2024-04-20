cities={
    'rio' : {
        'country' : 'brazil',
        'population' : '6.748 million',
        'fact' : 'Rio is the largest Portuguese city outside of Portugal',
    },
    'capetown' : {
        'country' : 'south africa',
        'population' : '4.618 million',
        'fact' : 'Table Mountain is a part of national park',
    },
    'san francisco' : {
        'country' : 'united states of america',
        'population' : '815,201',
        'fact' : 'It is home to the world most crooked street',
    },
}
print("My favourite cities:")
for city, infos in cities.items():
    print(f"\nCity: {city.title()}")
    country_of_origin=f"{infos['country']}"
    population_of_city=f"{infos['population']}"
    fact_about_city=f"{infos['fact']}"
    print(f"\tCountry: {country_of_origin.title()}")
    print(f"\tPopulation of the city: {population_of_city}")
    print(f"\tFact about city: {fact_about_city}")