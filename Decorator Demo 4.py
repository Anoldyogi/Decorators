'''Smart use of functions'''

def decor(func):
	def inner(a,b):
		if b==0:
			print("Sorry b cant be zero")
		else:
			func(a,b)
	return inner
@decor
def display(a,b):
	print(a/b)

display(15,3)
display(15,0)
