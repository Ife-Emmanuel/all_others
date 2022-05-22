# #EXERCISE 6-7
# people = [ {
#     'first_name' : 'Ifeoluwa',
#     'last_name' : 'Babalola',
#     'age' : 20,
#     'city' : 'ibadan',
# },
#
# {
#     'first_name' : 'gboyega',
#     'last_name' : 'oyetola',
#     'age' : 20,
#     'city' : 'osogbo',
# },
#
# {
#     'first_name' : 'teslim',
#     'last_name' : 'folarin',
#     'age' : 20,
#     'city' : 'lagelu',
# },
#
# ]
#
# print('Heading' + '  ::  ' + 'detail')
# for user_info in people:
#     if user_info:
#         for heading, detail in user_info.items():
#             print(heading + '  ::  ' + str(detail))
#         print('\n')
#
# print('==========================================')
# #EXERCISE 6-8
#
# pets = [
#
#     {'dog' : {
#         'kind' : 'domestic',
#         'owner\'s name' : 'Bayo',
#             }
#     },
#
#     {'hen' : {
#             'kind' : 'poultry',
#             'owner\'s name' : 'Jide',
#             }
#     },
#
#     {'cat' : {
#             'kind' : 'cadon',
#             'owner\'s name' : 'Bisola',
#             }
#     },
#
# ]
#
# for pet in pets:
#     if pet:
#         for name, details in pet.items():
#             print('The features of a ' + name + ' are:')
#             print('features  ::  value')
#             for index, (feature, value) in enumerate(details.items()):
#                 print(str(index + 1) + '. ' + feature + ' :: ' + value)
#             print('\n ')
#
#
# # But guys for real, programming is damn cool.
# print('===================================================')

#EXERCISE 6-9

# favourite_places = {
#     'dayo' : ['moniya',],
#     'busayo' : ['olodo', 'iworoad', 'iyanachurch',],
#     'nafisat': ['alarere', 'ogbomoso'],
#     'lukman' : []
#                     }

# for name, places in favourite_places.items():
#     if len(places) == 1:
#         print(name.title() + '\'s favourite place is ' + places[0].title())
#     elif len(places) > 1:
#         print(name.title() + '\'s favourite places are :' )
#         for index, place in enumerate(places):
#             print( str(index + 1) + '. ' + place.title())
#     else:
#         print(name.title() + ' entered no favourite place(s)')
#     print('\n')
#
# print('============================================')

#EXERCISE 6-10

# f

#EXERCISE 6-11

cities = {
    'ibadan' : {
        'country' : 'nigeria',
        'state' : 'oyo',
        'secretariat' : 'gate',
        'population' : 22
            },


    'ikeja' : {
        'country' : 'nigeria',
        'state' : 'lagos',
        'secretariat' : 'cms',
        'population' : 25
            },

    'osogbo' : {
            'country' : 'nigeria',
            'state' : 'osun',
            'secretariat' : 'cena house',
            'population' : 13,
                },

}
#
# print('The data for the following cities are taken: ')
# for city in cities:
#     print(city)
#     for city_info, stated in city.items():
#         print( city + '\'s ' + city_info + ' :: ' + stated )

print('The data for the following cities are taken: ')
for city, details in cities.items():
    print(city)
print('\n')
for city, details in cities.items():
    for city_info, stated in details.items():
        print( city + '\'s ' + city_info + ' :: ' + str(stated) )
    print('\n')

print(list((cities.items())))
dict_list = list((cities.items()))
print(dict_list[0][0])
print(len(dict_list))

#CREATING TABLES
# for city, details in cities.items():
#     for city_info, stated in details.items():
#         print('city   country   state   secretariat   population')
        #print(city + city)

print('city   country   state   secretariat   population')
i = 0
j = 0
length = len(dict_list)

for i, j in range(length):
    for m, n in range(length):
        print(dict_list[0][0])