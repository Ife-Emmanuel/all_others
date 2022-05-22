# alien_0 = {'colour' : 'green', 'points' : '5'}
# print(alien_0['colour'])
# alien_0['colour'] = 'red'
# alien_0['height'] = 21
# print(alien_0)
# alien_0.update({'size':29})
# print(alien_0)
# new_point = alien_0['points']
# print('You just earned ' + str(new_point) + 'points')
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

alien_0 = {'colour' : 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print('===========================')
alien_0 = {'colour': 'green'}
print('The alien is ' + alien_0['colour'] + '.')
alien_0['colour'] = 'yellow'
print('The alien is now ' + alien_0['colour'] + '.')

print('==========================')

alien_0 = {'point': 0, 'x_position': 0, 'y_position': 25, 'speed': 'medium'}
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
for i in range(10):
    alien_0['x_position'] = alien_0['x_position'] + x_increment

print('New x-position: ' + str(alien_0['x_position']))

print(alien_0)
del alien_0['point']
print(alien_0)

favourite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
    }

print('Sarah\'s favourite language is ' +
      favourite_languages['sarah'].title()+
      '.')

print('=========================================')
friends = [ 'jen', 'paul', 'edward','daniel']
for name in favourite_languages.keys():
    print(name)
    if name in friends:
        print('Hi '+ name.title() + ', I see your favourite'
                                    'language is '+
                                    favourite_languages[name] )
for friend in friends:
    if friend not in favourite_languages.keys():
        print(friend.title() + ', please take our poll!')

print('====================================')
for name in sorted(favourite_languages.keys()):
    print(name.title() + ', thank you for taking the poll')

# print(favourite_languages.values())
# print(favourite_languages.keys())
print('================================================')
print('Here are the counts of polled languages')
for language in set(favourite_languages.values()):
    print(language + ' :: ' + '%d' %list(favourite_languages.values()).count(language))