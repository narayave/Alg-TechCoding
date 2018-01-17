#
# Definition for binary tree:
# class Tree(object):
#	def __init__(self, x):
#	  self.value = x
#	  self.left = None
#	  self.right = None

# Code fights Trees: Basic

def hasPathWithGivenSum(t, s):
	# Possibly to recursively solve. 
	# Need to pass a branch of tree, and subtract value from sum

	if t == None:
		return False
	s = s - t.value
	print s
	
	if t.left == None and t.right == None:
		if s == 0:
			return True
		else:
			return False
			
	if t.left != None:				   # Left tree can be explored
		print t.value, s
		return hasPathWithGivenSum(t.left, s)
	else:
		print t.value, s
		return hasPathWithGivenSum(t.right, s)