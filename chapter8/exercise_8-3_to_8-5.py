# # #EXERCISE 8-3
# #
# # def make_shirt(size= 23, message= 'The Rock' ):
# #     print('Make me a shirt of size ' + str(size) + ' with ' +
# #           message + ' printed on it.')
# #
# # make_shirt(22, 'The Bouncer')
# #
# # make_shirt()
# # make_shirt(21, 'kelvin land')
# # make_shirt(message= 'Burberry', size= 82)
# #
# # make_shirt(size= 'Large', message= 'I love Python')
# # make_shirt(size= 'medium')
# # make_shirt(size= 55, message= 'Wonderland')
# #
# # def describe_city(city_name= 'Ibadan', country= 'Nigeria'):
# #     print(city_name + ' is in ' + country)
# #
# # describe_city('Ikeja', 'London')
# # describe_city(country= 'America', city_name= 'miami')
#
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = last_name + ' ' + first_name
#     return full_name.title()
#
# musician = get_formatted_name(last_name= 'babalola', first_name= 'ifeoluwa')
# print('Musician name is ' + musician + '.')
#
# a = 'Babalola Ifeoluwa Emmanuel'
# print(a.split(' '))
# print(' '.join(a.split(' ')))
# a = [ ' a ', 'b', 'c', 'd']
# print(''.join(a))

#To make optional arguments for functions
# def get_formatted_name(first_name, last_name, granni_name= '', middle_name=''):
#     """Return a full name, neatly formatted."""
#     if granni_name:
#         full_name = last_name + ' ' + first_name + ' ' +  middle_name + ' ' + granni_name
#     else:
#         full_name = last_name + ' ' + first_name + ' ' + middle_name
#     return full_name.title()
#
# first_student_name = get_formatted_name('adewale','daniel', 'temiloba')
# print(first_student_name)
#
# second_student_name = get_formatted_name('babalola', 'emmanuel', granni_name='ifeoluwa', middle_name= 'ajiloba', )
# print(second_student_name)

def formatted_name(first_name, last_name, middle_name= ''):
        if middle_name:
            full_name = first_name + ' ' + middle_name + ' ' + last_name + '.'
        else:
            full_name = first_name + ' ' + last_name
        return full_name.title()


musician = formatted_name('ayodeji', 'balogun', 'Temitope')
print(musician)
footballer = formatted_name('akinola', 'busayo')
print(footballer)

persons = []
def buildperson(firstname, lastname, age= ''):
    """Return a dictionary of information about a person."""
    if age:
        person = {'first': firstname, 'second': lastname, 'age' : age}
    else:
        person = { 'first' : firstname.title(), 'second' : lastname.title(), 'age' : 'Nil'}
    persons.append(person)
    return person

# musician = buildperson('teslim', 'fatimat', age=23)
# print('======================================================')
# print(musician)
# print(persons)

while True:
    print('Enter \'q\' anytime to quit')
    firstname = input('Enter firstname : ')
    if firstname == 'q':
        break
    lastname = input('Enter lastname : ')
    if lastname == 'q':
        break
    age = input('age : ')
    buildperson(firstname, lastname, age)
print(persons)

print('{:<12}{:<12}{:<12}'.format('Lastname', 'Firstname', 'Age'))

i = 0
alist = []
for i in range(len(persons)):
    list = []
    for element in persons[i].values():
        list.append(element)
    alist.append(list)

for (a, b, c) in alist:
    print('{:<12}{:<12}{:<12}'.format(a, b, c))












