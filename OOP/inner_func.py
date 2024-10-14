def double_decker():
    print("Starting the double decker function here")
    def inner_decker():
        print("Inside the inner decker")
        return "Zisan dadu"
    return inner_decker

# print(double_decker())
print(double_decker()())


def do_something(work):
    print("Work Starting")
    # print(work)
    work()
    print("Work Ending")

# do_something(2)

def coding():
    print("Sodanipoar python re")

do_something(coding)