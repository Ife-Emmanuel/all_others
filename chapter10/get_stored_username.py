"""functions that returns username if present else returns None """
import json
def get_stored_user_name():
    file_name = 'username.json'
    username = json.load(file_name)
    if username:
        return username
    else:
        return None
