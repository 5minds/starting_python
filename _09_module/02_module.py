
from os import name, environ as env
# from os import * # !!! niemals auch wenn andere das machen!!!

print name
print env['PATH']
# print env['path'] # KeyError
print env.get('path')
