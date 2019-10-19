#Demo program 2 for decorator function

def decor(func):
    def inner(a,b):
        print('#'*50)
        print('Sum =',end='')
        func(a,b)
        print('#'*50)
    return inner

@decor
def sum(a,b):
    print(a+b)

sum(1,2)
