class Solution(object):
	def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		"""
		if x < 0:
			return False
		y = str(x)
		size = len(y)

		if size == 1:
			return True
		y = y[::-1]
		x = str(x)
		# y = eval(y)
		# print x, y
		for i in xrange(size):
				if x[i] != y[i]:
					return False

		return True