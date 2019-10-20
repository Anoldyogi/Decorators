def decor1(func):
	def inner1():
		print('Inner-1')
		func()
	return inner1

def decor2(func):
	def inner2():
		print ('inner-2')
	return inner2

@decor1
@decor2
def wish():
	print('Wish')

wish()