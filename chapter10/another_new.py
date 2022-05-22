import json
def get_new_username():
    filename = 'my_username.json'
    user_name = input('Enter a user_name : ')
    with open(filename, 'w') as file_object:
        json.dump(user_name, file_object)
    return user_name

