class Shopping:
    cart = []
    origin = "China"
    
    def __init__(self, name, location) -> None:
        self.name = name
        self.location = location
        
    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f"Buying: {item} for price: {price} and remaining: {remaining}")
    
    @staticmethod
    def multiple(a, b):
        res = (a*b)
        print(res)
        
    @classmethod
    def hudai_deki(self, item):
        print(f"Hudai deki {item} kintu kinbo na")
        
        
Shopping.purchase("a", 1, 3, 5)

basundhara = Shopping("Bashundhara", "jani na")
basundhara.purchase(1, 3, 5)
basundhara.hudai_deki("Lungi")

Shopping.hudai_deki("Lungi")
basundhara.multiple(3, 3)
Shopping.multiple(4, 6)