# EXERCISE 7-8 Deli
# sandwich_orders = ['banana', 'orange', 'flower', 'pawpaw']
# finished_sandwiches = []
# for sandwich in sandwich_orders:
#     print('I made you ' + sandwich + 'sandwich')
#     finished_sandwiches.append(sandwich)
#
# print('The are the completed sandwiches')
# for sandwich in finished_sandwiches:
#     print(sandwich)


##EXERCISE 7-9 No Pastrami
# sandwich_orders = ['banana', 'pastrami',  'orange', 'pastrami', 'flower', 'pawpaw', 'pastrami']
# finished_sandwiches = []
# for sandwich in sandwich_orders:
#     print(sandwich)
# print('Deli has run out of pastrami')
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# for sandwich in sandwich_orders:
#      print('I made you ' + sandwich + 'sandwich')
#      finished_sandwiches.append(sandwich)
# print('The are the completed sandwiches')
# for sandwich in finished_sandwiches:
#     print(sandwich)

#EXERCISE 7-10 Dream Vacation
active = True
destination = []
while active:
    vacation = input('What is your dream vacation : ')
    destination.append(vacation)
    print('I will take you to ' + vacation)
    response = input(r'Do you have someone else? (Y\N) ')
    if response == 'N':
        active = False

print('The list of your favourite travel destination are : ')
for index, place in enumerate(destination):
    print(str(index + 1) + '. ' + place.capitalize())




