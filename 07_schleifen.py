

times = 5

while True:
	print "hello "
	times -= 1
	if times == 0:
		break

for i in (1, 2, 3):
	print "hello %s" % (i)

print "-" * 50
print [1] * 10

for i in range(5, 10, 2):
	print "hello %s" % (i)

print "-" * 20

a = [1] * 5
for x in a:
	print x
