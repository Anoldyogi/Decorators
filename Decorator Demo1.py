def decor(func):
    def inner():
        print("Inner")
        print("Inner")
    return inner

@decor
def display():
    print("display")

display()
