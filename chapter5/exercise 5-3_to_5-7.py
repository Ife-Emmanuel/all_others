# alien_colour='green'
# if alien_colour=='green':
#     print('You just earned 5 points')
# else:
#     print('You just earned 10 points')
#
alien_colour='green'
if alien_colour=='green':
    print('You just earned 5 points')
elif alien_colour=='yellow':
    print('You just earned 10 points')
elif alien_colour=='red':
    print('You just earned 10 points')

print('========================')

age=157

if age<2:
    print('You are a baby')
elif age>=2 and age<4:
    print('You are a toddler')
elif age>=4 and age<13:
    print('You are a kid')
elif age>=13 and age<20:
    print('You are a teenager')
elif age>=20 and age<65:
    print('You are an adult')
elif age>=180:
    print('You must be dead or a fraudster')
else:
    print('You are a very old person')

favourite_fruits=['mango','orange','banana']
#favourite_fruits=['man','ora','ban']
fruit=input('Enter a fruit: ')
#if fruit[0:3] in favourite_fruits:
if fruit in favourite_fruits:
    print('You really like '+fruit)
else:
    print('Are you just getting some interest in '+fruit)

