#usernames = ['eric','kathy','karen','admin','david']
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hi {}, thank you for loggin in again.".format(username))
else:
    print("Something's wrong with the usernames")