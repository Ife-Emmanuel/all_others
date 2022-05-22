# class Dog():
#     """A simple attempt to model a dog"""
#     def __init__(self, name, age):
#         """Initialize name and age attributes"""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """Simulate a dog sitting in response to a command"""
#         print(self.name.title() + ' is now sitting.')
#
#     def roll_over(self):
#         """Simulate rolling over in response to a command"""
#         print(self.name.title() + 'rolled over!')

class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def fill_gas_tank(self):
        work = 'The gas has been filled'
        return work

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())

class battery:
    """A simple attempt to model a battery for a car"""

    def __init__(self, battery_size= None):
        self.battery_size = battery_size

    def describe_battery(self, weight):
        """Print a statement describing the battery size."""
        print('This car has a ' + str(self.battery_size) + ' -kWh battery.')
        print('The weight of the battery is ' + str(weight))

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        else:
            active = True
            while active:
                print('You have entered a correct battery size.')
                self.battery_size = input('Please enter a standard size : (70, 85, 80, 90)')
                print('Your battery is not a standard battery.')
                if self.battery_size:
                    active = False

        message = 'This car can go approximately ' + str(range)
        message += 'miles on a full charge'
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
        else:
            self.battery_size = 85


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print('This car doesn\'t have gas tanks.')


my_exercisecar = ElectricCar('toyota', 323, 2018)
my_exercisecar.battery.get_range()
print('============')
my_exercisecar.battery.upgrade_battery()
my_exercisecar.battery.get_range()
my_tesla = ElectricCar('tesla', '5', 2016)
print('===========================================')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery(34)
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print(my_tesla.fill_gas_tank())
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print('===================')
my_tesla.battery.get_range()



