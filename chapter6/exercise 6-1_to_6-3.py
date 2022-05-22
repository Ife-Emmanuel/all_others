
my_info = {
    'first_name': 'Ifeoluwa',
    'last_name': 'Babalola',
    'age': 20,
    'city': 'ibadan'
}
print('First name is ' + my_info['first_name'])
print('I live in ' + my_info['city'])

print('My information:' )
print('Details  ::  response' + '\n')
for key, value in my_info.items():
    print(str(key) + '  ::  ' + str(value))

print('===========================================')
favourite_numbers = {'ife': 2, 'bayo': 5, 'kemi': 3}
for name, number in favourite_numbers.items():
    print(name.title() + ' :: ' + str(number))

print('=========================================')

glossary = {
            'print': 'Use to provide output of a executed command to the screen',
            'input': 'Used to get input from a user',
            'for': 'Used to iterate over a sequence'
            }

for word, meaning in glossary.items():
    print(word + ':\n\t' + meaning)
