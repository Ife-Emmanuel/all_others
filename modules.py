def table_creation_from_dictionary_in_list(list1):
    """It converts a list with dictionary contents into
    into a list chain ready to for conversion to table."""
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

#module practice
# students = [
#     {'name' : 'Babalola', 'score' : 89, 'matric no' : 98777},
#     {'name' : 'kolapo', 'score' : 73, 'matric no' : 895422},
#     {'name' : 'adebayoo', 'score' : 67, 'matric no' : 545321},
#     {'name' : 'sodiya', 'score' : 77, 'matric no' : 238738},
#             ]
# ammendedstudents = table_creation_from_dictionary_in_list(students)
# print(ammendedstudents)
#
# print('{:<4}{:<12}{:<12}{:<12}'.format('S/N', 'Name', 'Score', 'Matric no'))
#
# while students:
#     for i, (a, b, c) in enumerate(ammendedstudents):
#         print('{:<4}{:<12}{:<12}{:<12}'.format(i + 1, a, b, c))
#     else:
#         break






#print(__doc__(table_creation_from_dictionary_in_list))

import pandas

 
