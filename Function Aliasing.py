def Wish(name):
    print("GM",name)

#Function aliasing
Greetings=Wish

Wish('Sunny')
Greetings('Sunny')

#Id of Wish and Greetings is same.
print(id(Wish))
print(id(Greetings))


print(Wish)
print(Greetings)


#Deleting one function, still we can use other
del Wish
Greetings("Vinny")
