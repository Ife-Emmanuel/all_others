#sandwich_items = ['burberry', 'clasa', 'juicy', 'dango']

def sandwiches(*sand_items):
    print('Your sandwich has the following items included : ')
    for i, item in enumerate(sand_items):
        print(str(i + 1) + '. ' + item)

sandwiches('butter', 'clasak', 'berry', '23cent')

##Exercise8-13
def build_profile(first, last, **userinfo):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    profile.update(userinfo)
    return profile

print(build_profile('ifeoluwa', 'babalola', age=12, school='University of Ibadan'))


def carinfo(manufacturer_name, model_name, **otherinfo):
    info = {}
    info['manufacturer_name'] = manufacturer_name
    info['model_name'] = model_name
    info.update(otherinfo)
    return info

car = carinfo('toyota', 'sienna', colour= 'red', tow_package= True)
print(car)

