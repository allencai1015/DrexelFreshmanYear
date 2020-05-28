class Vehicle(object):

    def __init__(self, color, doors, tires, vtype):
        self.color = color
        self.doors = doors
        self.tires = tires
        self.vtype = vtype

    def brake(self):
        return "The %s is braking!" % self.vtype

    def drive(self):
        return "I'm driving a %s %s!" % (self.color, self.vtype)

class Car(Vehicle):

    def brake(self):
        return "The car class is breaking slowly!"
    
car1 = Car("yellow", 2, 4, "car")
print(car1.brake())
print(Vehicle.brake(car1))
car2 = Car()
print(car2.color)