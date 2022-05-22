alien_0 = {'colour' : 'green', 'points' : 5}
alien_1 = {'colour' : 'yellow', 'points' : 10}
alien_2 = {'colour' : 'red', 'points' : 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print('===============================================')

#Make an empty list for storing aliens.
aliens = []
print(type(aliens))

for alien in range(30):
    new_alien = {'colour' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)


for alien in aliens[:5]:
    print(alien)
print('...')

print('Total number of aliens: ' + str(len(aliens)))

for alien in aliens[0:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

    elif alien['colour'] == 'yellow':
        alien['colour'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

print('===========================================')

pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheese'],
}

print('You ordered a ' + pizza['crust'] + '-crust pizza ' +
      'with the following toppings: ')
for toppings in pizza['toppings']:
    print('\t' + toppings)

favourite_languages = {
    'jen' : ['python', 'ruby'],
    'sarah' : ['c'],
    'edward' : ['ruby'],
    'dara' : [],
}

for name, languages in favourite_languages.items():
    if len(languages) == 1:
        print(name.title() +("'s"if name[len(name) - 1] != 's' else "'") +
              ' favourite language is ' + languages[0])
    elif len(languages) > 1:
        print(name.title() + ("'s" if name[len(name) - 1] != 's' else "'") +
              ' favourite languages are: ')
        for language in languages:
            print(language)
    else:
        print(name.title() + ', you probably have not entered your favourite langauges. Please do.')

#Dictionary inside dictionary

users = {
    'ainstein' : {
        'first' : 'albert',
        'last' : 'einstein',
        'location' : 'princeton',
        },

    'mcrurie' : {
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'paris',
     }
}

print(users)

for username, user_info in users.items():
    print('\nUser\'s full name : ' + username.title())
    full_name = user_info['first'] + '' + user_info['last']
    location = user_info['location']

    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + location.title())
