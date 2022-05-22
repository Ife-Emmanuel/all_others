# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1
#
# prompt = '\nTell me something, and I will repeat it back to you: '
# prompt += '\nEnter \'quit\' to end the program: '
# message = ''
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

active = True
prompt = '\nTell me something, and I will repeat it back to you.'
prompt += '\nEnter \'quit\' to end the program: '
while active:
    message = input(prompt)
    if message.lower() == 'quit' :
        active = False
        print('Game Over')
    else:
        if message != 'quit':
            print(message + '\n')
    exclaimation = 'Again '

    if len(exclaimation) < len('Again '*3):
        exclaimation = exclaimation + 'Again '
        prompt = exclaimation + prompt

#How to make the player play the game again if he is interested
#in playing again. Is it break or the flag

