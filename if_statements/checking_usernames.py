current_users=['alina', 'aigerim', 'amina', 'helen', 'john']
new_users=['Alina', 'AIGERIM', 'roman', 'diana', 'fara']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Please enter new username {new_user}")
    if new_user.lower() not in current_users:
        print(f"Username is available for {new_user}")