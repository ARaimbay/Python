def city_country(city, country):
    full_info=f"{city}, {country}"
    return full_info.title()
first_pair=city_country('lima', 'peru')
print(first_pair)
second_pair=city_country('almaty', 'kazakhstan')
print(second_pair)
third_pair=city_country('rio','brazil')
print(third_pair)