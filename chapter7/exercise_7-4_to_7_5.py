# active = True
# prompt = 'Enter the pizza topping(s) you want : \n'
# while active:
#     topping = input(prompt)
#     if topping == 'quit':
#         active = False
#     else:
#         print('Dear customer ' +
#               topping.title() + ' will be added to ' +
#               'your topping')
#         prompt = ''
# print('All your requested toppings are being added.')

active = True
prompt = 'Do you want to get ticket(Y / N) : '
while active:
    response = input()
    if response.title() == 'N':
        print('Thanks for the poll. Allow other users ' +
              'to give response')
    age = int(input('Enter your age : \n'))
    if age < 3:
        ticket = 0
    elif age < 12:
        ticket = 10
    elif age > 12:
        ticket = 15
    print('The cost of your ticket is ' + '$' +
          str(ticket)+ '.')
    prompt = 'Wanna get ticket(Y / N) : '






