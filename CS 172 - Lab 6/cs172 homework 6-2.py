# Type code here
import sys

class ItemToPurchase():
    def __init__(self, item_name = "none", item_description = "none", item_price = 0, item_quantity = 0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)
        
    def print_item_cost(self):
        self.cost = int(self.item_price * self.item_quantity)
        return "{} {:.0f} @ ${:.0f} = ${}".format(self.item_name, self.item_quantity, self.item_price, self.cost)
        
    def print_item_description(self, ItemToPurchase):
        return "{}: {}".format(ItemToPurchase.item_name, ItemToPurchase.item_description)
        
class ShoppingCart() :
    def __init__(self, name = "none", date = "January 1, 2016"):
        self.customer_name = name
        self.current_date = date
        self.cart_items = []
        
    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
        
    def remove_item(self, ItemToPurchase) :
        if ItemToPurchase in self.cart_items :
            self.cart_items.remove(ItemToPurchase)
        else :
            print("Item not found in cart. Nothing removed.")
        
    def modify_item(self, ItemToPurchase, new_quant):
        if ItemToPurchase in self.cart_items :
            ItemToPurchase.item_quantity = new_quant
        else :
            print("Item not found in cart. Nothing modified.")
            
    def get_num_items_in_cart(self):
        x = 0
        for item in self.cart_items :
            x += item.item_quantity
        return x
        
    def get_cost_of_cart(self):
        prices = []
        for x in self.cart_items :
            charge = x.item_price * x.item_quantity
            prices.append(charge)
        return sum(prices)
        
    def print_total(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        length = self.get_num_items_in_cart()
        print("Number of Items: {}\n".format(length))
        if length <= 0 :
            print("SHOPPING CART IS EMPTY")
            cost = self.get_cost_of_cart()
            print("\nTotal: ${}".format(cost))
        else :
            for item in self.cart_items :
                print(item.print_item_cost())
            cost = self.get_cost_of_cart()
            print("\nTotal: ${:.0f}".format(cost))
            
    def print_descriptions(self):
        print("{}'s Shopping Cart - {}\n".format(self.customer_name, self.current_date))
        print("Item Descriptions")
        for item in self.cart_items:
            print(item.print_item_description(item))

if __name__ == "__main__":
    name = input("Enter customer's name:\n")
    date = input("Enter today's date:\n")
    cart1 = ShoppingCart(name, date)
    
    print("\nCustomer name: {}".format(name))
    print("Today's date: {}".format(date))
    
    def print_menu(ShoppingCart: ShoppingCart) :
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit\n")
        option_select(ShoppingCart)
        
    def option_select(ShoppingCart):
        option = input("Choose an option:\n")
        if option == "q":
            sys.exit()
        if option == "o":
            print("OUTPUT SHOPPING CART")
            ShoppingCart.print_total()
            print_menu(ShoppingCart)
        elif option == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            ShoppingCart.print_descriptions()
            print_menu(ShoppingCart)
        elif option == "a":
            print("ADD ITEM TO CART")
            name1 = input("Enter the item name:\n")
            description1 = input("Enter the item description:\n")
            price1 = float(input("Enter the item price:\n"))
            quantity1 = int(input("Enter the item quantity:\n"))  
            Item1 = ItemToPurchase(name1, description1, price1, quantity1)
            
            ShoppingCart.add_item(ItemToPurchase = Item1)
            print_menu(ShoppingCart)
        elif option =="r":
            print("REMOVE ITEM FROM CART")
            remove = input("Enter name of item to remove:\n")
            temp = ShoppingCart.get_num_items_in_cart()
            for item in ShoppingCart.cart_items :
                if item.item_name == remove :
                    ShoppingCart.remove_item(item)     
            if ShoppingCart.get_num_items_in_cart() == temp:
                print("Item not found in cart. Nothing removed.")
            print_menu(ShoppingCart)
        elif option == "c":
            print("CHANGE ITEM QUANTITY")
            change = input("Enter the item name:\n")
            new = int(input("Enter the new quantity:\n"))
            for item in ShoppingCart.cart_items :
                if item.item_name == change :
                    ShoppingCart.modify_item(item, new)
            if (item.item_name == change) not in ShoppingCart.cart_items :
                print("Item not found in cart. Nothing modified.")
            print_menu(ShoppingCart)
        else:
            option_select(ShoppingCart)
            
    print_menu(cart1)
            
    
    




