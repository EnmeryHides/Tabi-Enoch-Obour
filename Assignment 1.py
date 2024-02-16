current_users = ('Kwame', 'Yaw', 'Tuesday', 'Ama', 'Lord')
new_users = ('Monday', 'Tuesday', 'Wednesday', 'Thurday', 'Kwame')

for new_user in new_users:
    print(new_user)
    if new_user in current_users:
        print(f" {new_user} This name already exist")
    else:
        print('Welcome ' + new_user)
