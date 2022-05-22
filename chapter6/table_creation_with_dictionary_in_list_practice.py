employees = [
     {'Name' : 'Alan Turing', 'age' :  25, 'salary' : 10000},
     {'Name' : 'Sharon Lin', 'age' : 30, 'salary' : 8000},
     {'Name' : 'John Hopkins', 'age' : 18, 'salary': 1000},
     {'Name' : 'Mikhali Tal', 'age' : 40, 'salary' : 15000}
 ]

adnew_tuple = []
for i in range(3):
    new_tuple = []
    for value in employees[i].values():
        new_tuple.append(value)
    adnew_tuple.append(new_tuple)
print(adnew_tuple)


def takefirst(employee):
    return employee[0]

def takesecond(employee):
    return employee[1]

def takethird(employee):
    return employee[2]
print('====================================================')
print('Alphabetical Order Rank')
print('{:<14}{:<14}{:<14}'.format('Name', 'Age', 'Salary'))
for (a, b, c) in sorted(adnew_tuple):
    print('{:<14}{:<14}{:<14}'.format(a, b, c))
print('\n')

print('Age Rank')
print('{:<14}{:<14}{:<14}'.format('Name', 'Age', 'Salary'))
for (a, b, c) in sorted(adnew_tuple, key=takesecond, reverse= True):
    print('{:<14}{:<14}{:<14}'.format(a, b, c))
print('\n')

print('Salary Rank')
print('{:<14}{:<14}{:<14}'.format('Name', 'Age', 'Salary'))
for (a, b, c) in sorted(adnew_tuple, key=takethird, reverse= True):
    print('{:<14}{:<14}{:<14}'.format(a, b, c))
print('\n')





