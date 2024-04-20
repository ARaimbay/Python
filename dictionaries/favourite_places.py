favourite_places={
    'aigerim' : ['capetown', 'vancouver', 'rio'],
    'john' : ['los angeles', 'san francisco'],
    'alice' : ['almaty'],
}
for users, places in favourite_places.items():
    print(f"\n{users.title()}'s favourite places are:")
    for place in places:
        print(f"\t{place.title()}")