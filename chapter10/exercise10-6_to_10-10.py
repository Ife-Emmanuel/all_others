# """EXERCISE 10-6"""
# def addition():
#     try:
#         first_number = int(input('Enter the numerator : '))
#         second_number = int(input('Enter the denominator : '))
#         result = first_number + second_number
#     except ValueError:
#         print('Invalid input. Ensure to enter an number not letters.')
#     except TypeError:
#         print('Please enter integers for both numerator and denominator')
#     else:
#         print(result)
#
# addition()

"""EXERCISE 10 - 7  Addition Calculator"""

#
# def addition():
#     print('Enter "N" to quit.')
#     while True:
#         try:
#             first_number =int(input('Enter the numerator : '))
#             second_number = int(input('Enter the denominator : '))
#             # if first_number or second_number == 'N':
#             #     break
#             result = first_number / second_number
#         except ZeroDivisionError:
#             pass
#         except ValueError:
#             print('Invalid input. Ensure to enter a number not letters.')
#         except TypeError:
#             print('Please enter integers for both numerator and denominator')
#         else:
#             print(result)
#
# addition()







#29

#
# """EXERCISE 10 - 8 Cats and Dogs : """
# filenames = [
#             r'‪C:\Users\User\Documents\cats.txt',
#             r'‪C:\Users\User\Documents\EMMA DRAWING_recover000.dwg'
#             ]
#
# for filename in filenames:
#     with open(filename, encoding= 'utf-8', errors= 'ignore' ) as file_object:
#         content = file_object.read()
#         print(content.rstrip())

"""EXERCISE 10-10. Common Words : """
"""To count how many times a particular word or phrase appears in a string."""

line = 'Row, row, row your boat'
a = line.count('row')
print(a)
a = line.lower().count('row')
print(a)

print('ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ')

filename = r'C:\Users\User\PycharmProjects\python_crash_course\chapter10\text_files\Alice_in_Wonderland.txt'
with open(filename, encoding= 'utf-8')  as file_object:
    content = file_object.read()
    word_count = content.lower().count(' the ')
print('The number of words in ' + filename
      + ' is ' + str(word_count))





