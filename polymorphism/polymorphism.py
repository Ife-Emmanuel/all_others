#Overriding a variable

class Parent:
    name = 'scott'

class Child(Parent):
    pass

obj = Child()
print(obj.name) # David