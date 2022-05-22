# class Restaurant:
#     """Simple attempt to model a restaurant"""
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         """Simulate the description of a restaurant"""
#         print(self.restaurant_name.title() + ' has been created.')
#         print('It has a ' + self.cuisine_type + 'd structure')
#
#     def open_restaurant(self):
#         print('Hey ' + self.restaurant_name.title() + ' is open.')
#
#
# first_restaurant = Restaurant('boulloud', 'garret')
# print(first_restaurant.restaurant_name)
# print(first_restaurant.cuisine_type)
#
# first_restaurant.describe_restaurant()
# first_restaurant.open_restaurant()
#
# print('=======================================')
# list = []
# thefirst = Restaurant('yakoyo', 'egedu')
# list.append(thefirst)
# thesecond = Restaurant('colabase', 'cafeteria')
# list.append(thesecond)
# thethird = Restaurant('indomie', 'shop')
# list.append(thethird)
#
# for restaurant in list:
#     restaurant.describe_restaurant()
#     print('============================')
# thesecond.describe_restaurant()
# thethird.describe_restaurant()

class Users:
    """Simple attempt to model a user"""
    def __init__(self, first_name, last_name):
        """Initializing attributes as a reference to instances"""
        self.first_name = first_name
        self.last_name = last_name
        self.fullname = self.first_name + ' ' + self.last_name
        self.level = 100
        self.hall = 'Bello'

    def describe_user(self):
        """Definiton of method for the class"""
        print('User details : ' +
              '\nFullname = '  + self.fullname.title() +
              '\nOther info : ' +
              '\nLevel : ' + str(self.level) +
              '\nHall of Residence : ' + self.hall)

    def greet_user(self):
        """Definiton of method for the class"""
        print('Hello ' + self.fullname.title() + '. You are welcome!')

users = []
first_user = Users('Ifeoluwa','Babalola')
users.append(first_user)
second_user = Users('Roland','Adetimehin')
users.append(second_user)
third_user = Users('lukman','Adegoke')
users.append(third_user)

for user in users:
    user.describe_user()
    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    user.greet_user()
    print('================================')






