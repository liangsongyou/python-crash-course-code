current_users = ['david','dawn','karen','malissa','christine']
new_users = ['David','robert','jake','eli','karen']

for user in new_users:
    if user.lower() in current_users:
        print("{} already exists. Please try a new username.".format(user))
    else:
        print("{} is availabel".format(user))
