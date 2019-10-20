def decor1(func):
	def inner1():
		print("Inner 1")
		func()
	return inner1

def decor2(func):
	def inner2():
		print("inner 2")
		func()
	return inner2


@decor2
@decor1
def f1():
	print('f1')

f1()