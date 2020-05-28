class Item:
    def __init__(self, __name: str, __price: float, __taxable: bool):
        self.__name = __name
        self.__price = __price
        self.__taxable = __taxable
        
    def __str__(self):
        return "{}, {}, {}".format(self.__name, self.__price, self.__taxable)
        #https://pythonprogramming.net/__str__-__repr__-intermediate-python-tutorial/
    
    def getPrice(self):
        return self.__price
    
    def getTax(self, __tax_rate):
        tax = self.__price * __tax_rate
        return tax

class Receipt:
    def __init__(self, tax_rate = 0.07, purchases = []):
        self.__tax_rate = tax_rate
        self.__purchases = purchases
     
    def __str__(self):
        return "{}".format(self.__tax_rate)
    
    def addItem(self, Item):
        self.__purchases.append(Item)
        
#Main Program
if __name__ == "__main__" :
    r = Receipt()
    print("Welcome to Receipt Creator")
    
    def input_item():
        name = input("Enter Item name: ")
        price = float(input("Enter Item Price: "))
        tax = input("Is the item taxable (yes/no): ")
        if tax == "yes" :
            new_item = Item(name, price, True)
        else :
            new_item = Item(name, price, False)
        r.addItem(new_item)
        
        more = input("Add another item (yes/no): ")
        if more == "yes":
            input_item()
        else :
            print("----- Receipt time -----")
            subtotal = 0
            tax = 0
            for item in r._Receipt__purchases:
                print('{:_<20}{:_>20.2f}'.format(item._Item__name, item.getPrice()))
                subtotal += item.getPrice()
                if item._Item__taxable == True :
                    tax += item.getTax(r._Receipt__tax_rate)
            total = subtotal + tax
            
            print('\n{:_<20}{:_>20.2f}'.format("Sub Total", subtotal))
            print('{:_<20}{:_>20.2f}'.format("Tax", tax))
            print('{:_<20}{:_>20.2f}'.format("Total", total))
            print()
            
    input_item()
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    