# #Overloading Methods
#
# class Human:
#     def sayHello(self, name=None):
#         if name is not None:
#             print('Hello ' + name)
#         else:
#             print('Hello')
#
# obj = Human()
# obj.sayHello()
# obj.sayHello('Bola')

class Bird:
    def fly(self, name= None):
        a = name
        if a == 'parot':
            print('Can Fly')
        if a == 'penguine':
            print('Cannot fly')
        if a is None:
            print('No input')

obj = Bird()
obj.fly('penguine')

