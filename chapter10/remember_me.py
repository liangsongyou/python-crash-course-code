import json

def get_stored_username():
    """Retrieve the username from file if it exists."""
    file_p = 'username.json'
    try:
        with open(file_p) as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username    

def get_username():
    """If the name doesn't exist in file. Try this."""
    file_p = 'username.json'
    username = input('What is your name? ')
    with open(file_p,'w') as file:
        json.dump(username,file)
        print('We\'ll remember you when you come back {}.'.format(username.title()))

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        is_name = input("Is {} your name?[y/n] ".format(username))
        if is_name == 'n':
            get_username()
        else:
            print('Welcome back, {}'.format(username))
    else:
        username = get_username()
    
if __name__ == '__main__':
    greet_user()