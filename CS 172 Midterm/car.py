class Car:

    def __init__(self,make = "Unknown", model = "Unknown", year = 2020):
        self.__make = make
        self.__model = model
        self.__year = year

    def __str__(self):
        return "Make: " + self.__make + " Model: "+ self.__model

    def getMake(self):
        return self.__make

    def getModel(self):
        return self.__model

    def getYear(self):
        return self.__year

    def setMake(self,make):
        self.__make = make

    def setModel(self,model):
        self.__model = model

    def setYear(self,year):
        self.__year = year
  
car1 = Car("Nissan", "360Z", 2018)
car2 = Car("Toyota", "Corolla")
car2.setYear(2019)
car2.setYear(2020)
car2.setYear(2018)

car3 = Car()
car3.setModel(car2.getModel())
car3.setModel(car1.getModel())
car4 = Car("Tesla", "Model X")

car5 = Car("Tesla", "Model X")

car1 = car5
print(car1.getYear())