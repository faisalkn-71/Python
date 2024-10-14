class Calculator:
    brand = "casio ES999"
    price = 'no jani'
    
    def add(self, num1, num2):
        res = num1 + num2
        return res
    
    def sub(self, num1, num2):
        res = num1-num2
        return res
    def mul(self, num1, num2):
        res = num1*num2
        return res
    def div(self, num1, num2):
        res = num1/num2
        return res
    
work = Calculator()

add = work.add(1, 2)
print(add)

sub = work.sub(3, 2)
print(sub)

mul = work.mul(3,2)
print(mul)

div = work.div(6, 2)
print(div)