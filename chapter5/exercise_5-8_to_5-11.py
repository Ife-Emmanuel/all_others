#usernames=['bayo','admin','Lukman','tolu','paul']
usernames=[]
if usernames:
    for name in usernames:
        if name == 'admin':
            print('Hello admin, would like to see a status report')
        else:
            print('Hello '+name+', thankyou for logging in again ')
else:
    print('We need to find some users!')

print('=============================================')

current_users=['femi', 'simi', 'john', 'dotun', 'kemi']
new_users=['Simi', 'salawu', 'Kemi', 'balogun']
for user in new_users:
    if user.lower() in current_users:
        print('User name used\nEnter a new username: ')
    else:
        print('Username available')
    print('==============')

print('=========================================')

indices=[1, 2, 3, 4, 5, 6, 7, 8, 9]
for index in indices:
    if index == 1:
        print(str(index)+'st')
    elif index == 2:
        print(str(index)+'nd')
    elif index == 3:
        print(str(index)+'rd')
    else:
        print(str(index) + 'th')
