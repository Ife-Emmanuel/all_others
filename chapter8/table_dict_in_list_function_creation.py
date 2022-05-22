students = []
while True:
    dict = {}
    print('Enter \'q\' to quit.')
    student_name = input('Enter your name : ')
    if student_name == 'q':
        break
    matric_no = int(input('Enter your matric number : '))
    if matric_no == 'q':
        break
    score = int(input('Enter your score : '))
    if score == 'q':
        break
    dict.update({'name': student_name.title(), 'matric_no' : matric_no, 'Score' : score})
    students.append(dict)

print(students)


def dict_in_list_table_append(list1):
    listappend2 = []
    for i in range(len(list1)):
        dict = list1[i]
        def firstappend(dict):
            listappend1 = []
            for value in dict.values():
                listappend1.append(value)
            return listappend1
        listappend1= firstappend(dict)
        listappend2.append(listappend1)
    return listappend2

students_in_list_form = dict_in_list_table_append(students)
### Now to create tables
print('{:<5}{:<20}{:<15}{:<15}'.format('S/N','Student name', 'matric no', 'score'))
for i, (a, b, c) in enumerate(students_in_list_form):
    print('{:<5}{:<20}{:<15}{:<15}'.format(str(i + 1) + '.', a, b, c))










