#Overriding Methods

class Bank:
    def rate_of_interest(self):
        return 0

class ICICI(Bank):
    pass
    # def rate_of_interest(self):
    #     return 10.5

obj = ICICI()
print(obj.rate_of_interest())

obj1 = Bank()
print(obj1.rate_of_interest())
