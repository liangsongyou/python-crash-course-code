# start with a list of unconfirmed users 
# and an empty list to hold confirmed users

unconfirmed_users = ['alice','bob','martin','hansel']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("Verifying user: {}".format(current_user))
    confirmed_users.append(current_user)


# printing names of confirmed users
print("The following users have been confirmed:")
for user in confirmed_users:
    print("{}".format(user.title()))