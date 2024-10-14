class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name 
        self.age = age
        self.height = height
        self.weight = weight
        
    def eat(self):
        print("ajaira kana fina sob")

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight =weight
        self.team = team
    def eat(self):
        print("They are on a good deit")
    
    def __add__(self, other):
        return self.age + other.age
    
    def __mul__(self, other):
        return self.height * other.height

    def __len__(self):
        return self.height

sakib = Cricketer("Sakib", 40, 111, 90, "BD")
mushi = Cricketer("Mushi", 42, 100, 80, "BD")

# print(sakib.eat())


print(7+6)        
print("Guran" + "Laoshi")
print([12, 5] + [1, 2, 3, 4, 5])
print(sakib+mushi)
print(sakib*mushi)
print(len(sakib))