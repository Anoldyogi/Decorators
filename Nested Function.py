#Nested Function

def outer():
    print("Outer Started")
    def inner():
        print("Inner")
    inner()
    print("Outer completed")
    

outer()
#below will give error as this inner function is local to outer function only
inner()
