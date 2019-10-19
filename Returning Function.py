# A Function can return another Function
def outer():
    def inner():
        print("Inner")
    return inner


'''outer function is getting executed and it is returning inner function object,
which is getting assinged to f1.
Now f1 and inner pointing to same object'''
f1=outer()
f1()
