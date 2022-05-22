responses = {}
polling_active = True

while polling_active:
    name = input('\nWhat is your name? ')
    response  = input('Which mountain will you like climb someday: '
                      '')

    responses[name] = response

    #find out if anyone else is going to take the poll.
    repeat = input('Would you like to let another person respond? (yes/No)')
    if repeat == 'no':
        polling_active = False

print('\n------------Poll Results')
for name, response in responses.items():
    print( name.title() + ' would like to climb ' + response + '.')