#DO NOT CHANGE THIS CODE IN ANY WAY
class Building():
    def __init__(self,address,owner=None):
        self.__address = address
        self.__owner = owner
    
    def __str__(self):
        return str(self.__address) + " is owned by " + str(self.__owner)
    
    def getOwner(self):
        return self.__owner
    
    def getAddress(self):
        return self.__address
        
    def setOwner(self, owner):
        self.__owner = owner


#TODO  Your BuildingForSale class
class BuildingForSale(Building):
    def __init__(self, address, value, owner=None, isAvailable= True):
        super().__init__(self)
        self.__value = value
        self.__isAvailable = isAvailable
        
    def isAvailable(self):
        return self.__isAvailable
        
    def getValue(self):
        return self.__value
    
    def __str__(self):
        if self.isAvailable():
            return "{} is owned by {} and is being sold for ${}.".format(Building.getAddress(self), Building.getOwner(self), self.__value)
        else :
            return "{} is owned by {} and is NOT for sale.".format(Building.getAddress(self), Building.getOwner(self))
    
    def putOnMarket(self, value):
        self.__isAvailable = True
        self.__value = value
    
    def sell(self, value, owner):
        self.__value = value
        self.setOwner(owner)
        self.__isAvailable = False

x = BuildingForSale("1234", 2000)
x.setOwner("Matt")
print(x)