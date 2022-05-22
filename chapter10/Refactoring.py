import json

def greet_user():
    """Greet the user by name."""
    filename = 'username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        with open(filename, 'w') as file_object:
            username = input('Enter your name : ')
            json.dump()
            print(username.title() + ', your name will be remembered the next time you login.')
    else:
        print(username.title() + '. Welcome again!')

greet_user()