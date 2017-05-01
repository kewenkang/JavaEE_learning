import functools
import sys


def log(*arg):
	def decorator(func):
		@functools.wraps(func)
		def swapper(*args, **kw):
			for a in arg:
				print a
			print "begin call %s" % (func.__name__)
			func(*args, **kw)
			print "after call %s" % (func.__name__)
		return swapper
	return decorator
	
@log("exec","sss")
def now():
	print "now"

now()
print now.__name__