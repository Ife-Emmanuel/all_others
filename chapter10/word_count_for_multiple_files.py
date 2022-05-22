"""Using a function to determine the numbers of
of words in a number of files."""
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding= 'utf-8', errors= 'ignore' ) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        msg = 'Sorry, the file + ' + filename + 'does not exist.'
        print(msg)
    else:
        # Count the approximate number of words in the file.
        with open(filename, 'a+', encoding='utf-8', errors='ignore') as file_object:
            words = content.split()
            file_object.write(('\n'.rstrip() * 5).rstrip() + 'The rough estimate of the number of words in the content is ' + str(len(words)))


filename = r'C:\Users\User\PycharmProjects\python_crash_course\chapter10\text_files\Alice_in_Wonderland.txt'
count_words(filename)
