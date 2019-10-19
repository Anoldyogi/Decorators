#Uuse of function inside a function

list1=[1,2,3,4,5,6,7,8,9,10]

def is_even(n):
        if n%2==0:
            return True
        else:
            return False

list2=list(filter(is_even,list1))
print(list2)
