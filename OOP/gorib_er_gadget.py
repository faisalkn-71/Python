class Gadget:
    def __init__(self, brand, price, color) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        
    def run(self):
        return f"Running: {self.brand}"
        

class Laptop:
    def __init__(self, memory, ssd) -> None: 
        self.memory = memory
        self.ssd = ssd
    
    def coding(self):
        return f"Learning Python and Practicing"

class Phone(Gadget):
    def __init__(self, brand, price, color, duel_sim) -> None:
        self.duel_sim = duel_sim
        super().__init__(brand, price, color)
    
    def phone_call(self, number, text):
        return f"Sending SMS to: {number} with: {text}"
    
    def __repr__(self) -> str:
        return f"Phone: {self.brand} {self.price} {self.duel_sim}"
    
class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel
        
    def change_lens(self):
        pass
    

my_phone = Phone("iPhone", 120000, "Black", True)
print(my_phone.brand)
print(my_phone)
        
         
        