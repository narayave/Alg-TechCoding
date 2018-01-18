# Codefights
# Common Techniques: Basic
# sumOfTwo

def sumOfTwo(a, b, v):

	if a == [] or b == []:
		return False

	a = sorted(a)
	b = sorted(b)

	# Trying out greedy algorithm here
	if len(a) < len(b):
		size = len(b)
		for i in xrange(size-1, -1, -1):
			leftover = v - b[i]
			if leftover <= 0:
				pass
			# print leftover, a
			if leftover in a:
				return True
		return False
	else:
		size = len(a)
		for i in xrange(size-1, -1, -1):
			leftover = v - a[i]
			if leftover <= 0:
				pass
			# print leftover, a
			if leftover in b:
				return True
		return False


	# Working for most tests, but supposedly failing 6.
	# Execution error that I don't know about.