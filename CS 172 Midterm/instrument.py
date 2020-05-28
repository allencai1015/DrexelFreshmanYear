class Instrument():
    def __init__(self, Type = "Guitar", Description = "No description given", Value = 0, Owner = "No owner", Model = "No model provided", Year = 0, SerialNumber = -1):
        self.__type = Type
        self.__description = Description
        self.__current_value = Value
        self.__owner = Owner
        self.__model = Model
        self.__year = Year
        self.__serial_number = SerialNumber
        
    def __str__(self):
        return "For Sale: {}, {}, Price: {}, Owner: {}, Model: {}, Year: {}, Serial Number: {}".format(self.__type, self.__description, self.__current_value, self.__owner, self.__model, self.__year, self.__serial_number)
    
    def getOwner(self):
        return "{}".format(self.__owner)
        
    def getValue(self):
        return self.__current_value
        
    def sell(self, name, value):
        self.__owner = name
        self.__current_value = value