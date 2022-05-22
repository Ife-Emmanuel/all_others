# def greet_user():
#
#     """Does he know anything about what I told you. No I dont think she does
#     she only do tha t"""
#     print('Hello!')
#
# greet_user()

# def outerfunction(text):
#     def innerfunction():
#         print(text)
#     return innerfunction
#
# a = outerfunction('Hello')
# del outerfunction
# #outerfunction('Hello')
# a

# school = 'Nickdel'
# def nth_power(exponent,name,school):
#     def pow_of(base):
#         print(name)
#         print(school)
#         print
#         return pow(base, exponent)
#     print(name)
#     return pow_of
#
# name = 'babalola'
# square = nth_power(2,name,school)(3)
# print(square)
# cube = nth_power(3, name,school)(2)
# print(cube)
# del nth_power
#
# def display_message():
#     print('I am learning and studying functions')
#
# display_message()
#
# def favourite_books(title):
#     print('One of my favourite books is ' + title)
#
# favourite_books('The observant girl')
#
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet"""
#     print('\nI have a ' + animal_type + '.')
#     print('My ' + animal_type + '\'s name is ' + pet_name.title() + '.')
#
# describe_pet('hamster', 'harry')
#
# describe_pet( pet_name= 'harry', animal_type= 'hamster')
#
# def pow(number):
#     return number**2
#
#
# a = [1, 4, 2, 3, 5, -4, -3, -2]
# print(sorted(a, reverse= True, key= pow))
#
# def describe_pet(pet_name = 'willie', animal_type = 'dog' , animal_class = 'domestic'):
#     print('I have a ' + str(animal_type ))
#     print('My ' + str(animal_type) + '\'s name is ' + pet_name)
#     print('And you all know it is a ' + animal_class + ' animal.')
#
# print('\n===========================================')
# describe_pet('oscar', 23, 'domestic')
# print('\n============================================')
# describe_pet('willie', animal_type= 23 , animal_class='domestic' )
# describe_pet('willie', animal_type= 'cattle' , animal_class='domestic' )
# #describe_pet('willie', 'dog', 'domestic')
# describe_pet(pet_name= 'jackie')
#
# def another(name, age = 5, school = 'amazing'):
#     print(name.title() + '\'s age is ' + str(age) + '. And he attends ' +
#           str(school) + ' college' )
#
# another('afeez', 22, 'yinbol')

def greet_users(names):
    '''Print a simple greeting to each user in the list.'''
    for name in names:
        msg = 'Hello, ' + name.title() + '!'
        print(msg)

usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)
#
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print('Printing : ' + current_design.title())
#     completed_models.append(current_design)
#
# print('Here is the list of completed models : ')
# for model in completed_models:
#     print(model)
#
def print_models(unprinted_designs, completed_models):
    a = unprinted_designs[:]
    while a:
        current_design =a.pop()
        print('Print : ' + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    for model in completed_models:
        print(model)

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)













#print(nth_power(3)(2))







