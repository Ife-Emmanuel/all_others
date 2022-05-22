#*********Try to investigate what could have course my result on the second line
#print(Counter(favourite_languages).most_common(3))**************
favourite_languages={
    'jen' : 'python',
    'sarah' :'C',
    'edward' : 'ruby',
    'phil' : 'python'
}

print('The following languages has been mentioned: ')
for language in favourite_languages.values():
    print(language.title())
newlist = ['ahmed', 'jen', 'kemi', 'sarah', 'edward', 'johnson']

if newlist:
    for name in newlist:
        if name in favourite_languages.keys():
            print(name + ', thankyou for responding to the poll')
        else:
            print(name + ', you are cordially invited to take the poll.')





print('=====================================')

from collections import Counter
#*********Try to investigate what could have course my result on the second line
#print(Counter(favourite_languages).most_common(3))
print(Counter(favourite_languages.values()).most_common(3))
print('====================')
print(type(favourite_languages))
a= [2,3,1,3,2,5,4]
print(type(a))
print(Counter(a).most_common(3)[0][0])






# #
# #
# # a = ['bab', 'adf', 23]
# # print(Counter(a))
# # print('===========================')
# # print(a.count('bab'))
#
#
# def student(name, **marks):
#     print(name)
#     for subject, mark in marks.items():
#         print(subject)
#         print(mark)
#
#
# student('Babalola', math = 34, eng = 13, chem = 54)
#
# print('========================================')


