import math
import time
def timer(func):
    def inner(*args, **kargs):
        print("Time Started")
        start = time.time()
        # print(func)
        func(*args, **kargs)
        print("Time Ended")
        end = time.time()
        print(f"Total time taken {end-start}")
    return inner

# timer()()

@timer
def get_factorial(n):
    print("Factorial Starting")
    result = math.factorial(n)
    print(f"Factorial of {n} is: {result}")

get_factorial(n=1500)

# timer(get_factorial)()