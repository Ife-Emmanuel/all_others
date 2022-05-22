userdetails = {
                'ife emmanuel' : 'babalola963',
                'akinsulire joshua' : 'akinjoh',
                'sobowale david' : 'davidsob',

            }

while True:
    print('Enter your account details below.')

    active = True

    for username, password in userdetails.items():
        usernameent = input('Username : ')
        passwordent = input('Password : ')
        if active:
            if usernameent != username:
                active = False
            elif passwordent != password:
                active = False

            print('Access Granted. Welcome to ubay.com' +
                  + '\nWelcome ' + usernameent +
                  '\nHere are the names of fellow member of ubay.com')
            for username in userdetails.keys():
                print(username)
            break
        else:
            print('Username or password incorrect.')
