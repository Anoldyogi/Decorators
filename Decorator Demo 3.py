'''calls the required function as per argument and prints the wish message'''

def decor(func):
	def inner(name):
		if name=='Sunny':
			print("Hello ",name)
			print('How are you')
		else:
			func(name)
	return inner
@decor
def display(name):
	print('hello',name,'GM')

display('Sunny')
display("Vinny")