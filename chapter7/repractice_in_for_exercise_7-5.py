####  READ ON HOW TO CONVERT LIST TO DICTIONARY IN PYTHON UNDER
#### DIFFERENT CONDITIONS.
active = True
prompt = 'Do you want to get ticket(Y / N) : '
a = []
tickets = []
while active:
    response = input(prompt)
    if response.title() == 'N':
        print('Thanks for the poll. Allow other users ' +
              'to give response')
        continue
    elif response.title() == 'Y':
        valid = True
        while valid:
            try:
                age = int(input('Enter your age : \n'))
                a.append(age)
            except Exception as e:
                print('Error occured : ', e)
            else:
                valid = False

        if age < 3:
            ticket = 0
        elif age < 12:
            ticket = 10
        elif age > 12:
            ticket = 15
        print('The cost of your ticket is ' + '$' +
              str(ticket)+ '.')
        tickets.append(ticket)

        prompt = 'Wanna get ticket(Y / N) : '
    else:
        continue
    if len(a) == 3:
        active = False

for age in a:
    print(age)
print('Hence the total sum of ticket purchased is ' + str(sum(a)))
