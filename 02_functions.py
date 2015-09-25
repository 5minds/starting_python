
def hello(name):
	"""params name: Gibt den Namen an.
	"""
	print "hello " + name

def hello_with_salutation(salutation="Hello", name="world"):
	print salutation + " " + name

def hello_with_kwargs(**kwargs):
	print kwargs['salutation'] + ' ' + kwargs['name']

hello("world")

hello_with_salutation("Hi")
hello_with_salutation("Hi", "5Minds")

hello_with_salutation(name="wir")

hello_with_kwargs(salutation='Hello', name='world')

hello('hello "')

h = hello

h("world")
print h.__name__
print h.__doc__
print dir(h)
