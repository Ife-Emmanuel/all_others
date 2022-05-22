employees = [
     {'Name' : 'Alan Turing', 'age' :  25, 'salary' : 10000},
     {'Name' : 'Sharon Lin', 'age' : 30, 'salary' : 8000},
     {'Name' : 'John Hopkins', 'age' : 18, 'salary': 1000},
     {'Name' : 'Mikhali Tal', 'age' : 40, 'salary' : 15000}
 ]


print(employees[0])

adnew_tuple= []
for i in range(3):
    new_tuple = []
    for value in employees[i].values():
        new_tuple.append(value)
    adnew_tuple.append(new_tuple)
    #print(new_tuple)

def takefirst(employee):
    return employee[0]
def takesecond(employee):
    return employee[1]
def takethird(employee):
    return employee[2]

print('The tables below shows the ranking of three employees based on their : \n')
print('1. Alphabetical order rank')
print('{:<14}{:<14}{:<14}'.format('Name', 'age', 'salary'))
for (a, b, c) in sorted(adnew_tuple):
    print('{:<14}{:<14}{:<14}'.format(a, b, c))
print('\n')

print('2. Age rank')
print('{:<14}{:<14}{:<14}'.format('Name', 'age', 'salary'))
for (a, b, c) in sorted(adnew_tuple, key= takesecond, reverse= True):
    print('{:<14}{:<14}{:<14}'.format(a, b, c))
print('\n')

print('3. Salary rank')
print('{:<14}{:<14}{:<14}'.format('Name', 'age', 'salary'))
for (a, b, c) in sorted(adnew_tuple, key= takethird, reverse= True):
    print('{:<14}{:<14}{:<14}'.format(a, b, c))






    # if i == 3:
    #     break





# print(employees[0])
# print('{:<14}{:<14}{:<14}')
# i = 0
# for employee in employees[i]:
#
#     new_tuple = []
#     adnew_tuple= []
#     for (a, b, c) in employees[i].items():
#         print('{:<14}{:<14}{:<14}'.format(a, b, c))
#     i += 1
#     if i == 3:
#         break
#






#     for key, value in employee.items():
#         res = (key, value) = key, value
#     new_tuple.append(res)
# for employee in employees[1:]

##You may need definitely need iterators here
#WATCH OUT EMMANUEL !!!

       #adnew_tuple.append(new_tuple)
#print(adnew_tuple)
# print('====================')
# print(new_tuple)
# for employee in adnew_tuple:
#     print(employee)