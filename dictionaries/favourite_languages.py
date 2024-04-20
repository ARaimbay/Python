favourite_languages={
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python',
}
names_for_poll=['edward', 'collin', 'harmony']
for name in favourite_languages.keys():
    print(f"Hi {name.title()}")
    if name in names_for_poll:
        print(f"Hello {name.title()}, please re-take a poll for this year!")
for name_for_poll in names_for_poll:
    if name_for_poll not in favourite_languages:
        print(f"Hi {name_for_poll.title()}, please take a poll for the first time!")