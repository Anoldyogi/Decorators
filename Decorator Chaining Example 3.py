def decor1(func):
    def inner1():
        x=func()
        return x*x
    return inner1

def decor2(func):
    def inner2():
        x=func()
        return x*2
    return inner2



@decor1
@decor2
def num():
    return 20
print(num())