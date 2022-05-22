"""EXERCISE 10-11 TO EXERCISE 10-13"""
import json
#EXERCISE 10-11 Favourite Number

def get_new_favourite_numbers():
    filename = 'favourite_number.json'
    favourite_number = int(input('Enter your favourite number : '))
    with open(filename, 'w') as file_object:
        json.dump(favourite_number, file_object)
    return favourite_number



def get_stored_favourite_number():
    filename = 'favourite_number.json'
    try :
        with open(filename) as file_object:
            favourite_number = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return favourite_number

def tell_favourite_number():
    favourite_number = get_stored_favourite_number()
    response = input('Is ' + str(favourite_number) + ' your favourite number? Enter (1/2) : ')

    if response == '1':
        print('I know your favourite number! It\'s ' + str(favourite_number))
    else:
        favourite_number = get_new_favourite_numbers()
        print('We\'ll remember your favourite number ' + str(favourite_number) + ' in your next login.')
        3
tell_favourite_number()

