#initializing custom list
cus_list = [4, 6]

#using dictionary comprehension to construct
# new_dict = {new_list : cus_list for new}


# using fromkeys() to construct


#simple example of dict_comprehension

dict = {str(i) : i for i in range(4)}

for key, values in dict.items():
    print(key,type(key), values, type(values))


#dict comprehension for length of names as keys for names in a list
list = ['babalola', 'femi', 'johnson', 'seyi']

dict = {len(name) : name for name in list}

for namelength, name in dict.items():
    print(name + ' :: ' + str(namelength))
for number in dict.keys():
    print(number)

print(dict.keys())

list1 = [10, 20, 4, 45, 99]
print('The largest number in the list : ' + str(max(dict.keys())))

fruits = ['orange', 'mango', 'banana', 'pawpaw']
dictionary = {f : i for f, i  in enumerate(fruits)}
print(dictionary)
revdict = {i : f for f, i in dictionary.items()}
print(revdict)




