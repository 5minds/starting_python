# encoding: utf-8
aBool = True # False
aInteger = 1

print 5/2 # Ergebnis 2 in Python 2.x 2.5 in Python 3
print 5/2. # Ergebnis 2.5

aLong = 1L
aDouble = 1.
aString = "hello world"
aTuple = (1, 2) # Unveränderliche Liste
aArray = [1, 2] # veränderliche Liste
aDict = {'erste': 1, 'zweite': 2}  # key => value Paare
aBytes = bytes("hello")
aUnicodeString = u"Hello wörld"

def hello_world():
	print "hello world"

aFunc = hello_world

aLamba = lambda name: "Hello %s" % (name) # Anonyme Funktion
print aLamba("world")
