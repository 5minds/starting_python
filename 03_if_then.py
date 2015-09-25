
a = None # entspricht null, nil, undefined, Nothing
a = True

if a:
	print "a is True"

b = 'hello 2'

# True: Nicht leere Zeichenkette, True, Zahlen != 0, nicht None

if b == 'hello':
	print "b is 'hello'"
elif b == 'hello 2' and a:
	print "b is 'hello 2'"
else:
	print "b is nicht 'hello'"
