users={
    'first_name' : ['aigerim', 'danara', 'asylzada'],
    'last_name' : ['raimbay', 'asluguzhiyeva', 'latif'],
    'age' : [34, 29, 30],
    'city' : ['chicago', 'perth', 'almaty'],
}
print(f"\nUsers full info:")
for user_info in users['first_name']:
    print(f"\tFirst name: {user_info}")
for user_info in users['last_name']:
    print(f"\tLast name: {user_info}")
for user_info in users['age']:
    print(f"\tAge: {user_info}")
for user_info in users['city']:
    print(f"\tCity: {user_info}")