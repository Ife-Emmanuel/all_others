a=['bola', 'von', 'bamise', 'taiwo', 'azeez', 'von', 'arise']
middle_list=[a[i] for i in range(len(a)//2 - (1 if len(a)%2==0 else 0),len(a)//2+1)]
print(middle_list)
a.pop()
middle_list=[a[i] for i in range(len(a)//2 - (1 if len(a)%2==0 else 0),len(a)//2+1)]
print(middle_list)
a=['peek', 'gig', 'peep', 'door']
#to determine the palindromes in the list
palindromes=[]
for name in a:
    if name == ''.join(list(reversed(name))):
        palindromes.append(name)
print(palindromes)
#Now to determine anagrams within a list - My trial
# str1='abcd'
# str2='dacb'
def anatest(str1,str2):
    if set(str1)==set(str2):
        return True
    else:
        return False

print(anatest('abcd','dabc'))
#Self trial lambda for indices of list element

testlist=['bola','bayo','taiwo','romoke','bayo']
print(list(filter(lambda i:testlist[i]=='bayo', range(len(testlist)) )))
#programming is very getting cool

a=[2,1,5,4,3,8,7,3]
print(len(a))
print('three items from the middle of the list are:')
mid=len(a)//2
mid2=len(a)//2-1
list=[]
for num in range(mid if len(a)%2==1 else mid2,mid+3):
    list.append(a[num])
    print (a[num])
#comprehension
middle=[a[i] for i in range(mid if len(a)%2==1 else mid2,mid+1)]
print(middle)
a=['bobo','akin','tunde','funmi']
#a=[3,2,1,5,4,7]
mid=len(a)//2
mid2=(len(a)//2)-1
middle=[a[i] for i in range(mid if len(a)%2==1 else mid2,mid+1)]
print(middle)

# for num in list:
#     print(num)

#initializing list
test_list=[1,3,4,3,6,7]
#printing initial list
print('Original list : '+ str(test_list))
#using enumerate() to find indices for 3
res_list=[i for i, value in enumerate(test_list) if value == 3]
#printing resultant list
print('New indices list : ' + str(res_list))#find

names=['jide', 'biodun', 'kazeem', 'azeez', 'biodun']
indices=[i for i, value in enumerate(names) if value== 'biodun']
print(indices)

#last three items
for name in names[-3:]:
    print(name)

mypizzas=['faa','a dad', 'daf', 'sae']
myfriends=mypizzas
print(mypizzas)
print(myfriends)
myfriends.append('new')
print(mypizzas)
print(myfriends)
thrfri=mypizzas[:]
print(thrfri)
thrfri.append('another')
print(thrfri)
another=tuple(mypizzas)
print(another)
a=[2,3,5,1,3]
b=str(a)
print(b)
print(b)
#print(mypizzas)
a='peep'
b='gig'
if reversed('peep')==a:
    print('object is a palindrome')
else:
    print('object is not a palindrome')
















