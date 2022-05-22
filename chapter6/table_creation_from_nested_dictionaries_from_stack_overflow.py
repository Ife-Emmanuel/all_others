###YOU STILL HAVE TO READ ON DATA STRUCTURES ON THE SAVED ON OPERAMINI
### IN YOUR PHONE
### ALSO...COMPLETE THE VOTING PLATFORM AND FIND BETTER MEANS TO SOLVE
### WHILE HAVING COMPLETED OTHER TOPICS
###LEARN HOW TO USE SUBLIME TEXT EDITOR AND GEANY ON APPENDIX B
###RUNNING ON PYTHON PROGRAMME ON A TERMINAL ON PAGE 16
dictionary = {
    'CA' : {
            'Bay Area' : [ ('warm?', 'yes\n') ,
                           ('East/West Coast?', 'West \n')],
            'SoCal' : [ ('north or south?', 'south \n'),
                        ('warm', 'yes \n'),]
            },
    'MA' : {
            'Boston' : [ ('East/West Coast?', 'East \n'),
                          ('like it there?', 'yes\n')],
            'Pioneer Valley' : [ ('East/West Coast?', 'East \n'),
                                 ('city?', 'no\n'),
                                 ('college town?', 'yes\n')]
            },
    'NY' : {
            'Brooklyn'  : [ ('East/West Coast?', 'East\n'),
              ('been there?', 'yes\n'),
              ('Been to coney island?', 'yes')],
            'Manhattan' : [ ('East/West Coast?', 'East \n'),
                            ('been there?', 'yes\n')],
            'Queens' : [ ('East/West Coast?', 'East \n'),
                         ('been there?', 'yes\n')],
            'Staten Island' : [('is island?', 'yes\n')]
            }
}

# for name, details in dictionary:
#     for city, ((a, b), (c, d), (e, f)) in details:









# print('If you tell us who you are, we can personalize the messages' +
# '\nWhat is your name')
# prompt = 'If you tell us who you are, we can personalize the messages'
# prompt += '\nWhat is your name : '
# print(input(prompt))


# import pandas as pd
# l = []
# for subd in dictionary:
#     l.append(pd.DataFrame(subd))

# headers = [ 'City', 'City2', 'East/West Coast?', 'north or south?', 'like it there?',]
#
# table = []
# for city in dictionary.keys():
#     for city2 in dictionary[city].keys():
#         new_row = [city]
#         new_row.append(city2)
#         for index_head in range(2, len(headers)):
#             found = False
#             for index in range(0, len(dictionary[city][city2])):
#                 if headers[index_head] in dictionary[city][city2][index]:
#                     found = True
#                     break
#                 if found:
#                     new_row.append(dictionary[city][city2][index][1].replace('\n', ''))
#                 else:
#                     new_row.append(' ')
#                     table.append(new_row)
#
# print(tabulate.tabulate(table, headers = headers, tablefmt= 'orgtbl'))