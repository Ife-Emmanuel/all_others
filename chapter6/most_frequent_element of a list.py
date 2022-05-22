# def most_frequent(list):
#     num = list[0]
#     counter = 0
#
#     for i in list:
#         if counter < list.count(i):
#             counter=list.count(i)
#             num = i
#     return num
#
# a= [2,3,1,2,4,2,3]
# print(most_frequent(a))
# import builtins
# a= [2,3,1,2,4,2,3]
# most_frequent = max(a, key= a.count)
# print(most_frequent)

from collections import Counter



