class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000
    
    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount>0:
            self.balance += amount
    
    def withdraw(self, amount):
        if amount<self.min_withdraw:
            print(f"Fokir! The minimum withdraw limit is {self.min_withdraw}")
        elif amount>self.max_withdraw:
            print(f"No mama No! The maximum withdraw limit is {self.max_withdraw}")
            
        else:
            self.balance -= amount
            print(f"{amount} has been debited from your account. Now your current balance is {self.get_balance()}")

usb = Bank(5000)
usb.deposit(5000)
print(usb.get_balance())

usb.withdraw(500000)

usb.withdraw(10)

usb.withdraw(1000)