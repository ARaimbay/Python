def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile=build_profile('aigerim', 'raimbay', education='MSc', location='chicago', gender='female')
print(user_profile)