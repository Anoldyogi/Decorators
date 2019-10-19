#We can pass function argument to another function
def f1(func):
    func()

def func():
    print("I am Func")

f1(func)
