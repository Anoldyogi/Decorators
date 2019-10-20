'''Calling same function with or without decorator'''

def decor(func):
	def inner(name):
		if name=='Sunny':
			print("Hey There! ",name)
		else:
			func(name)
	return inner

def wish(name):
	print('hi',name)

decorated_wish=decor(wish)


wish('Sunny')
wish('vinny')

decorated_wish('Sunny')
decorated_wish('Vinny')
