# #Reading a file
# file_path =  'text_files/new_text.txt'
# with open(file_path) as file_object:
#     file_content = file_object.read()
#     print(file_content.strip())
# print('---------------------')
#
# with open(file_path) as file_object:
#     lines = file_object.readlines()
#     for line in lines:
#         print(line)
#
#
# print(lines)

# file_path = 'text_files/new_text.txt'
# with open(file_path) as file_object:
#     lines = file_object.readlines()
#     pystrings = ''
#     for line in lines:
#         pystrings += line.strip()
#
# print(pystrings)
# print(type(pystrings))
# intnumber = int(pystrings)
# print(5 + intnumber)

# numbers = '8392328234'
# if '12' in numbers:
#     print('The numbers are contained in the first 12 '
#           'numbers of pi')
# else :
#     print('no they are not')

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write('I also love finding meaning in large datasets.\n')
    file_object.write('I love creating apps  that can run in a browser.\n')






