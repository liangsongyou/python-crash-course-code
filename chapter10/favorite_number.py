import json

def get_stored_number():
    """Get the number stored in file if any."""
    file_p = 'favorite.json'
    with open(file_p) as file:
        favorite = json.load(file)
    return favorite

def get_number():
    """Get the number from user if not available in file."""
    file_p = 'favorite.json'
    num = input("Enter your favorite number: ")
    with open(file_p,'w') as file:
        json.dump(num,file)

def favorite():
    """Display the favorite number of user if available otherwise ask for a number."""
    favorite = get_stored_number()
    if favorite:
        print('I know your favorite number! It\'s {}'.format(favorite))
    else:
        get_number()

if __name__ == '__main__':
    favorite()