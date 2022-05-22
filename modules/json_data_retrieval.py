import greet_user_get_stored_username_refactor
import another_new
def welcome_user():
    user_name = greet_user_get_stored_username_refactor.get_stored_username()
    if user_name:
        print('Welcome ' + user_name.title())
    else:
        user_name = another_new.get_new_username()
        print(user_name.title() + '. Your name will be remembered')








