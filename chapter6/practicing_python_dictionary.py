students = {
     'kemi' : [54, 64, 88, 72, 65],
     'lukman' : [71, 82, 76, 59, 91],
     'femi' : [23, 32, 43, 84, 23],
     'johnson' : [32, 98, 67, 81, 77]
 }

# print('{:<15}{:<12}{:<12}{:<12}{:<12}{:<12}'.format('name\n\subject', 'mathematics\n',
#                                'chemistry', 'physics', 'biology', 'english' ))
print('{:<12}{:<12}{:<12}{:<12}{:<12}{:<12}'.format('   subject', 'mathematics',
                               'chemistry', 'physics', 'biology', 'english' ))
print('{:<12}'.format('name'))
for name, (a, b, c, d, e) in students.items():
    print('{:<12}  {:<12}  {:<12}{:<12}{:<12}{:<12}'.format(name, a, b, c, d, e))

for name in list(students.keys()):
    print(len(name))

dict = {len(name) : name for name in students.keys()}
print('The lenth of the longest name is : ' + str(max(dict.keys())))
print(students.keys())








# listform = [len(name) for name in list(students.keys())]
# for len in listform:
#     print(len)
#
#
#
#
#
#
#
#
# # a = filter(lambda x : len(x) == max(listform), students.keys())
# # print(list(a))
