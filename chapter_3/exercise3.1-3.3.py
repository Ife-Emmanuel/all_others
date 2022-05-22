cars=['honda','camry','audi','toyota']
dict={}
i=0
while i<len(cars):
    dict.update({i:cars[i]})
    i+=1
print('My ordered purchase of cars:')
for keys,values in dict.items():
    print(str(keys+1)+'. '+values)

a=['Lukman','Joel','Israel']
print('Mr Joel wouldn\'nt be able to make it to the dinner.')
a[1]='salom'
print(a)
for friends in a:
    print(friends+', I hereby invite you to my dinner.')
print('Hello friends, I found a bigger place')
a.insert(0,'Samuel')
a.insert(2,'Taiwo')
a.append('Bolu')
print(a)
for friends in a:
    print(friends + ', I hereby invite you to my dinner.')

print('Hello guests, I have been informed that I can only invite two guests')
for i in range(len(a)-2):
    removed=a.pop()
    print('Sorry %s. You may not come for the dinner.'%a[len(a)-3])
#i=1
# for elements in range(2):
#     del a[i]
#     i-=1

#print(a)
# for elements in range(2):
#     a.pop()
# print(a)
i=1
while i>=0:
    del a[i]
    i-=1
print(a)