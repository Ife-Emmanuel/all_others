"""Functions that take in several files and tells the number of words in a file.
files that are not found are reported into missing_file.txt"""
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding= 'utf-8', errors= 'ignore') as file_object:
            content = file_object.read()
    except FileNotFoundError:
        with open('missing_files.txt', 'a') as file_object:
            file_object.write(filename + '\n')
         # print('Hello user, the file "' + filename + '" does not exist.')
    else:
        words = content.split()
        print('The file "' + filename + '" has about ' + str(len(words)) + ' words.')
        #return len(words)


def append_file(filename):
    words_number = count_words(count_words(filename))
    with open(filename, 'a', encoding= 'utf-8', errors= 'ignore') as file_object:
        print('The number of words in the file ' + filename + str(words_number))
        file_object.write('The number of words in the file ' + filename + str(words_number))


file_list = [
             r'C:\Users\User\PycharmProjects\python_crash_course\chapter10\arranged.txt',
             r'C:\Users\User\PycharmProjects\python_crash_course\chapter10\text_files\learning_python.txt',
             r'C:\Users\User\PycharmProjects\python_crash_course\chapter10\text_slots',
             r'C:\Users\User\PycharmProjects\python_crash_course\chapter10\firstpractice.txt',
             r'C:\Users\User\PycharmProjects\python_crash_course\chapter10\jerro.txt',
             r'C:\Users\User\PycharmProjects\python_crash_course\chapter10\text_files\Alice_in_Wonderland.txt'
             ]

with open('missing_files.txt', 'w') as file_object:
    pass
for filename in (file_list):
    count_words(filename)
    #print(str(i + 1) + '. ' + str(count_words(filename)))

print('\nAdmin, the following files are missing : ')
with open('missing_files.txt') as file_object:
    lines = file_object.readlines()
    for i, line in enumerate(lines):
        print(str(i + 1) + '. ' + line.rstrip())
print('program completed.')
##But really guys programming is the totally fun mehn...fucking fun
##Just love it.






