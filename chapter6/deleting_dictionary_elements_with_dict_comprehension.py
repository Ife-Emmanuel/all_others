#Wow programming is actually very cool guys!!!
students = {'lukman' : 24, 'wisdom' : 22, 'jerry' : 23, 'femi' : 32, 'adesua' : 14, 'elon' : 41}
print('students : ' + str(students))
remove_items = {'femi', 'jerry', 'kemi', 'folashade', 'johnson', 'sekemi'}
students = { key : students[key] for key in students.keys() - remove_items}
print('remove_items : ' + str(remove_items))
print('new students : ' + str(students))

