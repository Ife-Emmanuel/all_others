"""writing a program that prompts users for their name
and writing the response to file."""

print('Enter no if their is no more user. ')
i = 0
for i in range(5):
    i += 1
    name = input('Enter your name : ')
    if name == 'no':
        break
    with open('Guest', 'a') as file_object:
        file_object.write(str(i) + '. ' + name + '\n')

