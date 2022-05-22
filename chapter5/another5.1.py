str1='Father'
str2='father'
print(str1==str2)
print(str1.lower()==str2)
state='Oyo'
age=13
if age>=18 and state.lower()=='osun':
    print('you are eligible to vote')
# elif age>=18 and state.lower()!='osun':
#     print('You can vote but in osun state')
# elif age<=18 and state.lower()=='osun':
#     print('Sorry you are not yet up to 18.\nEndeavour to registered '
#           'once you are up to 18')
if age<18 or state!='osun':
    print('You are either not yet up to 18 or not an osun indigene')
# else:
#     print('You are not eligible to vote')
print('=============')
age=28
if age<4:
    price=0
elif age<18:
    price=5
elif age<60:
    price=3
elif age<70:
    price=0
print('Your admission price is $'+str(price)+'.')

requested_toppings=['mushroom','extracheese',]
if 'mushroom' in requested_toppings:
    print('adding mushroom')
if 'pepperoni' in requested_toppings:
    print('adding pepperoni')
if 'extracheese' in requested_toppings:
    print('adding extrachees')

print('=================')
requested_toppings=['mushroom','extracheese',]
if 'mushroom' in requested_toppings:
    print('adding mushroom')
if 'pepperoni' in requested_toppings:
    print('adding pepperoni')
if 'extracheese' in requested_toppings:
    print('adding extracheese')
print('\nFinish making your pizza')



