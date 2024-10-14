class Shop:
    cart = []
    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)
    
myself = Shop("Faisal Karim")
myself.add_to_cart("Phone")
myself.add_to_cart("Shoes")

print(myself.cart)

yourself = Shop("Yourself")
yourself.add_to_cart("Laptop")
yourself.add_to_cart("Bike")

print(yourself.cart)