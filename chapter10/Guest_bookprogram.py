"""Ask users for their name and print a greeting to the screen while adding a recording
of their visit to a file."""

with open('D:\Guest_book.txt', 'w') as file_object:
    print('Enter no if you are not visiting the ceremony.')

    print('Enter your name : ')
    i = 0
    while True:
        i += 1
        if i == 6:
            break
        name = input(str(i) + '. ')
        namelist.append(name)

with open('visitation_list.txt', 'w') as visitation_object:
    visitation_object.write('The following people visited the festival.\n')
    for i, name in enumerate(namelist):
        visitation_object.write(str(i + 1) + '. ' + name.title() + '\n')





        #file_object.write(name.title() + ' visited the festival.\n')

        #print('Welcome ' + name.title() + ' to the sport festival of today.')












