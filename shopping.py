class Shopping:
    def __init__(self, name):
        self.name = name   
        self.cart = []
    
    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)
        
    def remove_item(self, item_name):
        for product in self.cart:
            if item_name == product['item']:
                self.cart.remove(product)
                print(f"{item_name} successfully removed!")
            
        
    def checkout(self, amount):
        all_total = 0
        for item in self.cart:
            # print(item) 
            total = 0
            total += item['price'] * item['quantity']
            all_total += total
            print(f"the total amount for {item['item']} is {total} ")
            total=0
        # print("total is", all_total)
        
        if all_total>amount:
            print(f"Please! provide {all_total-amount} more")
        else:
            print(f"Please! take your extra {amount-all_total} money")
            
        

buyer = Shopping("M Anish")
buyer.add_to_cart("Condom", 50, 10)
buyer.add_to_cart("Rose", 100, 2)
buyer.add_to_cart("Chocklet", 150, 10)

# print(buyer.cart)
buyer.checkout(11500)


buyer.remove_item("Condom")
print(buyer.cart)


