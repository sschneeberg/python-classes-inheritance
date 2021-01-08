class Car():
    """ Car class displays car object with make model and color """ 
    def __init__(self, make, model, color):
        self.make =  make
        self.color = color
        self.model = model
        self.gas = 100

    def __str__(self):
        return "{},{},{}".format(self.make,self.model,self.color)

    def drive(self):
        self.gas -= 10
        print('vroommmm')

    def fill_tank(self):
        self.gas = 100
        print('Full!')

    def check_gas(self):
        print('Tank at:', self.gas, '%')


car1 = Car('Mercedes', 'C300', 'white')

car1.drive()
car1.drive()
car1.check_gas()
car1.fill_tank()
car1.check_gas()