
einfachen_string = "einfacher string"
multiline_string = """
m
ultiline
string
"""
multiline_string_2 = 'multiline\
string_\n2'

print einfachen_string
print multiline_string
print multiline_string_2

world = "world"
end = "!"

print "hello {0}{1}".format(world, end)
print "hello {world}{end}".format(world=world, end=end)
print "hello %s%s" % (world, end)

print "-----"
print einfachen_string[3:]
print einfachen_string[-1]
print einfachen_string[-4:]
print einfachen_string[3:6]
