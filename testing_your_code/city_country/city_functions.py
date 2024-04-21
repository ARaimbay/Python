def city_country_name (city, country, population = ''):
    """Function that accepts 2 parameters"""
    if population:
        city_country = f"{city}, {country}, and {population}"
    else:
        city_country = f"{city}, {country}"
    return city_country.title()