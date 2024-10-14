class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name
        self.__balance = initial_deposit
    
    def deposit(self, amount):
        self.__balance +=amount
    
    def get_balance(self):
        return self.__balance


fuck_shaheb = Bank("Fuck Shaheb", 10000)

print(fuck_shaheb.holder_name)
# print(fuck_shaheb.__balance)
print(fuck_shaheb.get_balance())
fuck_shaheb.deposit(5000)
print(fuck_shaheb.get_balance())