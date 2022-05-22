# def city_country(city_name, country):
#     city_descrip = city_name + ', ' + country
#     return '"' + city_descrip.title() + '"'
#
# first = city_country('london', 'england')
# second = city_country('washington', 'USA')
# third = city_country('ontario', 'canada')
# print(first)
# print(second)
# print(third)
#
#
def make_album(artist_name, album_title,number_of_tracks= ''):
    album = {}
    album['album_title'] = album_title
    album['artist_name'] = artist_name
    if number_of_tracks:
        album['number_of_tracks'] = number_of_tracks
    else:
        album['number_of_tracks'] = 'Nil'
    return album
#
# first = make_album('wizkid', 'olart')
# second = make_album('olamide', 'badho',3)
# third = make_album('peruzzi', 'keeke', number_of_tracks= 23)
#
# print(first)
# print(second)
# print(third)

dict_in_list = []
while True:
    print('Enter q in the question to break')
    artist_name = input('Enter the artist\'s name : ')
    if artist_name == 'q':
        break
    album_title = input('Enter the title of the album : ')
    if album_title == 'q':
        break
    number_of_tracks = input('Enter the number of tracks you have made : ')
    if number_of_tracks == 'q':

        break
    a = make_album(artist_name, album_title, number_of_tracks)
    dict_in_list.append(a)

print('S/N  {:<15}{:<15}{:<15}'.format('Artist name', 'Album Title', 'Number of tracks'))

# i = 0
# artist = []
# for i in range(len(dict_in_list)):
#     a = []
#     for value in dict_in_list[i].values():
#         a.append(value)
#     artist.append(a)
#
# for i, (a, b, c) in enumerate(artist):
#     print('{:<8}{:<15}{:<15}{:<15}'.format((i + 1),a, b, c))
    
    



###for converting a list which contains dictionaries into a list
# which has several list in it, in which the content of each list
# is the .values content of each dictionary in the initial list."""

list2 = []
def dict_in_list_table_append(object_list,list2):
    for i in range(len(object_list)):
        list1 = []
        def initial(object_list, list1):
            for value in object_list[i].values():
                list1.append(value)
            return list1

        list1 = initial(object_list, list1)
        list2.append(list1)
    return list2

print(dict_in_list)
a =dict_in_list_table_append(dict_in_list, list2)
print('====================================')
print(a)

for i, (a, b, c ) in enumerate(a):
    print('{:<5}{:<12}{:<12}{:<12}'.format((str(i+1) + '.'),a,b,c))


#'''s fdsasdf'''

