poll_list = {}
while len(poll_list) < 4:
    name = input('Enter your name : ')
    reason = input('Why do you like programming ? ')
    poll_list[name] = reason

    with open('poll_reasons.txt', 'a') as file_object:
        for i, (name, reason) in enumerate(poll_list.items()):
            file_object.write(str(i + 1) + '. ' + name + ' :: ' + reason + '\n')



