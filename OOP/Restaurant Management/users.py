#Customers 
#Employees
#Admin

from abc import ABC
from order import Order


class Users(ABC):
    def __init__(self, name, phone, email, address) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(Users):
    def __init__(self, name, phone, email, address) -> None:
        super().__init__(name, phone, email, address)
        self.cart = Order()
    
    def view_menu(self, restaurent):
        restaurent.menu.show_menu()
    
    def add_to_cart(self, restaurent, item_name, quantity):
        item = restaurent.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Item quantity exceeded!!")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
        else:
            print(f"{item} is not found")
    
    def view_cart(self):
        print("*****View Cart*****")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price : {self.cart.total_price()}")
    
    def pay_bill(self):
        print(f"Total {self.cart.total_price()} Paid Successfully!!")
        self.cart.clear()


class Employee(Users):
    def __init__(self, name, phone, email, address, age, designation, salary) -> None:
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary


# emp = Employee("M Anish", 2345678, "paul@brother.com", "Nepal", 39, "Captain", 1000000)

# print(emp.salary)
# print(emp.name)


class Admin(Users):
    def __init__(self, name, phone, email, address) -> None:
        super().__init__(name, phone, email, address)
    
    def add_employee(self, restaurent, employee):
        restaurent.add_employee(employee)
        
    def view_employee(self, restaurent):
        restaurent.view_employee()
    
    def add_menu_item(self, restaurent, item):
        restaurent.menu.add_menu_item(item)
    
    def remove_item(self, restaurent, item):
        restaurent.menu.remove_item(item)
        
    def view_menu(self, restaurent):
        restaurent.menu.show_menu()

      
# res = Restaurent("Haun Uncle er Bater Hotel")
# mn = Menu()
# item = FoodItem("Pizza", 12.34, 10)
# item2 = FoodItem("Burger", 10, 30)
# admin = Admin("Karim", 2345677, "karim@gmail.com", "CTG")
# admin.add_menu_item(res, item)
# admin.add_menu_item(res, item2)


# cust1 = Customer("Karim", 2345677, "karim@gmail.com", "CTG")
# cust1.view_menu(res)

# item_name = input("Enter item Name : ")
# item_quantity = int(input("Enter item quantity : "))

# cust1.add_to_cart(res, item_name, item_quantity)
# cust1.view_cart()