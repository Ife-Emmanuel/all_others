print('=======================')
requested_toppings=[]
print('Enter your favourite toppings\n'
                'Press "exit" if ok')
topping=input('Enter your favourite toppings: \n')
def topping():
    while topping!='exit':
        requested_toppings.append(topping)
        topping = input()
    if requested_toppings:
        for requested_topping in requested_toppings:
            print('Adding '+requested_topping +'.')
        print('Finished making your pizza')
    else:
        anwser = input('Are you sure you want a plain pizza Y/N:\n')
        if anwser == 'y':
            print('Finished making your pizza')
        else:
            topping()
topping=topping()





