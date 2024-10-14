def adder(*args):
    total = 0
    for num in args:
        total += num
    return total

print(adder(1, 2, 3))  
print(adder(4, 5))    
print(adder(10))   


def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", age=30, city="New York")

    
