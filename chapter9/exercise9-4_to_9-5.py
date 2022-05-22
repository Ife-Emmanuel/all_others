# class Restaurant:
#     """Simple attempt to model a restaurant"""
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         """Simulate the description of a restaurant"""
#         print(self.restaurant_name.title() + ' has been created.')
#         print('It has a ' + self.cuisine_type + 'd structure')
#
#     def open_restaurant(self):
#         print('Hey ' + self.restaurant_name.title() + ' is open.')
#
#     def set_numbers_served(self, numbers):
#          self.number_served = numbers
#
#     def increment_number_served(self, number):
#         self.number_served += number
#
#
#
# restaurant = Restaurant('yakoyo', 'alakat')
# print(str(restaurant.number_served) + ' customers has been served.')
# restaurant.number_served = 20
# print('======================')
# print(restaurant.number_served)
# restaurant.set_numbers_served(24)
# print('+++++++++++++++++++++++++')
# print(restaurant.number_served)
#
# for i in range(5):
#     restaurant.increment_number_served(4)
# print('============================')
# print(restaurant.number_served)


class User:
    """Simple attempt to model a user"""
    def __init__(self, first_name, last_name):
        """Initializing attributes as a reference to instances"""
        self.first_name = first_name
        self.last_name = last_name
        self.fullname = self.first_name + ' ' + self.last_name
        self.level = 100
        self.hall = 'Bello'
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


a_user = User('Atolagbe', 'toheeb')
for i in range(5):
    a_user.increment_login_attempts()

print(a_user.login_attempts)
a_user.reset_login_attempts()
print('==================================')
print(a_user.login_attempts)
