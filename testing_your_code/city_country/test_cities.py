from city_functions import city_country_name
def test_city_country_population():
    """Do like 'Santiago, Chile, and population xxx' work?"""
    city_country_population = city_country_name('Santiago', 'Chile', 'population=5000000')
    assert city_country_population == 'Santiago, Chile, And Population=5000000'