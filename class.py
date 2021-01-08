class Car():
    """ Car class displays car object with make model and color """ 
    def __init__(self, make, model, color):
        self.make =  make
        self.color = color
        self.model = model
        self.gas = 100

    def __str__(self):
        return "{}, {}, {}".format(self.make,self.model,self.color)

    def drive(self):
        self.gas -= 10
        print('vroommmm')

    def fill_tank(self):
        self.gas = 100
        print('Full!')

    def check_gas(self):
        print('Tank at:', self.gas, '%')

class Driver():
    """ Driver class displays a driver object with name, age, and driving style """
    def __init__(self, name, age, style):
        self.name = name
        self.age = age
        self.style = style
        self.car = ""

    def __str__(self):
        return "{}, {}, {}, {}".format(self.name, self.age, self.style, self.car)

    def honk(self):
        print('BEEEEEPPPP')

    def buy_car(self, car):
        self.car = car


car1 = Car('Mercedes', 'C300', 'white')

car1.drive()
car1.drive()
car1.check_gas()
car1.fill_tank()
car1.check_gas()

driver1 = Driver('Eunice', '84', 'Street Racer')
driver1.buy_car(car1)
print(driver1.__str__())
driver1.honk()

