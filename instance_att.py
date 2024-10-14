class Shop:
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []
    
    def add_to_cart(self, item):
        self.cart.append(item)
        
myself = Shop("Karim Md Faisal")
myself.add_to_cart("Phone")
myself.add_to_cart("Computer")
print(myself.cart)


yourself = Shop("YourSelf")
yourself.add_to_cart("Bike")
yourself.add_to_cart("Car")
print(yourself.cart)