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
#         """Simulate the opening of the restaurant"""
#         print('Hey ' + self.restaurant_name.title() + ' is open.')
#
#     def set_numbers_served(self, numbers):
#          self.number_served = numbers
#
#     def increment_number_served(self, number):
#         self.number_served += number
#
#
# class IcreamStand(Restaurant):
#     """An attempt to simulate a specific(Icecream type of
#     Restaurant)"""
#     def __init__(self, restaurant_name, cuisine_type, flavors):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = flavors
#
#     def display_flavors(self):
#         print('Here are the available flavors : ')
#         for i, flavor in enumerate(self.flavors):
#             print(str(i + 1) + '. ' + flavor)
#
#
# def listflavors():
#     print('Enter you the list of flavors available in stand')
#     list = []
#     for i in range(5):
#         a = input(str(i + 1) + '. ')
#         list.append(a)
#     return list
#
# firstlist = listflavors()
# first = IcreamStand('jennifer', 'renador', firstlist )
# print('=================================')
# first.display_flavors()

#EXERCISE 9-6

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

#EXERCISE 9-7

class Admin(Users):
    """An attempt to model an admin"""
    def __init__(self, privileges, first_name, last_name):
        super().__init__(first_name.title(), last_name.title())
        self.privileges = Privileges(privileges)



#EXERCISE 9-8

class Privileges:
    #privileges = ['dja', 'DJA', 'dfjsia']
    def __init__(self, privileges ):
        self.privileges = privileges

    def show_privileges(self):
        print('Admin privileges are : ')
        for i, privilege in enumerate(self.privileges):
            print(str(i + 1) + '. ' + privilege.title())

privileges = ['dja', 'DJA', 'dfjsia']
admin = Admin( privileges, 'lolade', 'taiwo')
print(admin.last_name)
admin.privileges.show_privileges()
print('===============================')
print(admin.fullname)


#EXERCISE 9-9 Battery Upgrade



#Guys I tell you programming is coool, in fucking cool









