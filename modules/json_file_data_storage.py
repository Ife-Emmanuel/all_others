"""module for storing users data.
data_name should be written in strings format."""
import json
def data_storage(data_name, data_value):
    filename = data_name + '.json'
    with open(filename, 'w') as file_object:
        json.dump(data_value, file_object)
    message = 'Your message has been stored.'
    return message


#Motherfucking wow!! while pass is a statement, None is an
##expression. They can both be used within a function


