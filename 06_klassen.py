
class BaseClass(object):

	def __init__(self, name="world"):
		self._name = name

	def printHello(self):
		print "Hello %s" % (self.name)

	@property
	def name(self):
		return self._name

aBase1 = BaseClass()
aBase1.printHello()

aBase2 = BaseClass("5Minds")
aBase2.printHello()

class OtherBaseClass(object):

	def __init__(self, name):
		pass

	def makeWat(self):
		print "yes I'can."

	def printHello(self):
		print "1>> Hello %s" % (self.name)

class DerivedClass(BaseClass, OtherBaseClass):

	def __init__(self):
		super(DerivedClass, self).__init__('Name')
		pass

aDerived = DerivedClass()
aDerived.printHello()
