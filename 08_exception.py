
try:
	raise Exception("a Error")
except Exception, e:
	print e
finally:
	print "finally"

print "-" * 20

try:
	pass
except:
	print "except"
else:
	print "no error raised"
