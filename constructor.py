class Phone:
    manufactured = "China"
    
    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price
        
my_phone = Phone("Karim Md Faisal", "Samsung", 120000)
print(my_phone.owner, my_phone.brand, my_phone.price)

other_phone = Phone("XYZ", "iPhone", 145677889)
print(f"Owner Name: {other_phone.owner} Brand Name: {other_phone.brand} Price: {other_phone.price}")