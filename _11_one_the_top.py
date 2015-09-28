
class MyClassAsAfunction(object):

	def __call__(self, **kwargs):
		print kwargs

def test_fkt():
	pass

def main():
	print callable(test_fkt)
	print callable(MyClassAsAfunction)
	a = MyClassAsAfunction()
	print callable(a)
	print a(name="name", value="value")

if __name__ == '__main__':
	main()
