pets={
    'kind' : ['cat', 'dog'],
    'owner' : ['aigerim', 'john'],
}
for pet in pets['kind']:
    print(f"\tKind: {pet}")
for pet in pets['owner']:
    print(f"\tOwner: {pet}")
