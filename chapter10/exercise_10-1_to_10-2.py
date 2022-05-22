with open(r'text_files/learning_python.txt') as file_object:
    lines = file_object.readlines()
for line in lines:
    line = line.replace('python', 'C++')
    print(line.rstrip())
print('yes completed')













    # for line in list(file_object)[:3]:
    #     print(line.rstrip())


#
# print(content)
# print(content)