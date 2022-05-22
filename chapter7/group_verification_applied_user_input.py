unconfirmed_users = [ 'alice', 'brian', 'candace', ]
confirmed_users = [ 'femi', 'sonekan', 'emmanuel']

def joingroup():

    print('verifying ' + current_user.title())
    confirmed_users.append(current_user)
    print('Admin has added ' + current_user + ' to the site')
    print(current_user + '  you can meet other users in the group\n')

print('Confirmed Users : \n' + str(confirmed_users))
print('\nUnconfirmed Users : ' + str(unconfirmed_users))

def leavegroup():
    if leave_request_name in confirmed_users:
        for index, object in enumerate(confirmed_users):
            if object == leave_request_name :
                exiter = confirmed_users.pop(index)
                print(exiter.title() + ', You have been successfully removed.\n')
            else:
                continue
    else:
        exiter =  leave_request_name
        print('You are not a member of the group.' +
              '\nOnly group members can exit group.')
    return exiter



while unconfirmed_users:
        active = True
        #To join group
        while active:
            current_user = unconfirmed_users.pop()
            if len(confirmed_users) > 6:
                print('Sorry ' + current_user + ' group is already filled.')
                active = False
            else:
                joingroup()
        # else:
        #     name = input('Enter a desired name for your account : ')
        #     unconfirmed_users.append(name)


print('\n####After accepting invitation for some to join###' +
      '\nConfirmed users: \n' + str(confirmed_users) + '\n')


#To leave the group
print('########LEAVE GROUP?#########')
response = input('Make sure you are a group member! ' +
                 '\nConfirm exit(Y/N) : ')
if response.title() == 'Y':
    leave_request_name = input('Enter your username if you want to leave group : ')
    exitername = leavegroup()

#prompting patronisers to attempt rejoining group
print('\n######PROMPTING SELF EXITED MEMBER TO REJOIN###')
print('Hello ' + exitername.title() + ' you can trying joining the group later.' +
          '\nYou can advertise your products and services here.\n')
print('########PROMPTING CURRENT USER TO JOIN LATER REJOIN.')
print('Hello ' + current_user + ' you can trying joining the group later.' +
          '\nYou can advertise your products and services here.\n')
print('########JOIN GROUP?#########')

##Asking for their response
response = input('Are you a new member and want to join group? (Y/N) : ')
if response.title() == 'Y':
    join_name = input('Enter a username : ')
    unconfirmed_users.append(join_name)
    print('You request is under verification. ')
    if len(confirmed_users) < 7:
        joingroup()




