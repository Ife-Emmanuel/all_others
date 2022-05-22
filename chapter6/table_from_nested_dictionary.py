users = {
     'ainstein': {
        'first' : 'albert',
        'last' : 'einstein',
        'location' : 'princeton',
        },

     'mcrurie': {
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'paris',
     }
}

print('=================================')
max = 0

def longestname(list):
    for name in list:
        length = len(name)
        global max
        if length > max:
            max = length
    return max

for name, details in users.items():
    print(name + '  :: ' + str(details))

for name in users.keys():
    print(name)

print(list(users.keys()))

# a = list(users.keys())
# for name in a:
#     print(name)
# print(a)
# maxlen = longestname(a)
# print(maxlen)
# for name, (first, last, location) in users.items():
#     print('{:<}

#To find the longest word using list comprehension
#
# long = [x for x in (list(users.keys) )]
# list(users.keys()).sort