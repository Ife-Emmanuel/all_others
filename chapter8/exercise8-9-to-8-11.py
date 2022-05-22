magicians = ['abaka', 'ijewo', 'demola', 'bashorun']

# def show_magicians(magicians_list):
#     for magician in magicians_list:
#         print(magician)
#
# show_magicians(magicians)
#
# def make_great(magicians_list):
#     new_list = magicians_list[:]
#     for magician in new_list:
#         magician = 'the Great ' + magician

def make_great(magicians_list):
    new_list = []
    while magicians_list:
        current_magician = magicians_list.pop()
        modified_magician = 'the Great ' + current_magician
        new_list.append(modified_magician)
    return sorted(new_list, reverse= True)


print('================================')
print(magicians)
print('new list unmodify: '  + str(make_great(magicians[:])))
print('new list modify' + str(make_great(magicians)))
print('original magicians list : ' + str(magicians))


def build_profile(first, last, **userinfo):
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    profile.update(userinfo)
    # for key, value in userinfo.items():
    #     profile[key] = value
    return profile

user_profile = build_profile('bobolla', 'atinuke', age= 23, school= 'bethel')
print(user_profile)
for info, value in user_profile.items():
    print(info + ' :: ' + str(value))
