class User:
    def __init__(self, name, age, money) -> None:
        self._name = name
        self._age = age 
        self.__money = money
    
    @property
    def salary(self):
        return self.__money
    
    @salary.setter
    def salary(self, value):
        if(value < 0):
            return "Salary can't be negative"
        self.__money += value
        

waktim = User("Guran Laoshi", 91, 5305)

# print(waktim.__money)
print(waktim._age)
print(waktim.salary)
print(waktim.salary)
waktim.salary = 5000
print(waktim.salary)