# Codefights
# Common Techniques: Basic
# sumOfTwo


def sumOfTwo(a, b, v):

    a = sorted(a)
    b = sorted(b)

    if len(a) < len(b):
        size = len(b)
    else:
        size = len(a)
    
    # Trying out greedy algorithm here
    for i in xrange(size-1, 0, -1):
        leftover = abs(v - b[i])
        print leftover, a
        if leftover in a:
            return True
    return False
	
if __name__ == '__main__':

	a = [4, 6, 4, 2, 9, 6, 6, 2, 9, 2]
	b = [3, 4, 5, 1, 4, 10, 9, 9, 6, 4]
	v = 5
	print sumOfTwo(a, b, v)
	
	# Working for most tests, but supposedly failing 9.
	# Execution error that I don't know about.