class Solution:
	# @param A : integer
	# @return a list of list of integers
	def generate(self, A):

		ret = []
		for i in xrange(0, A):
			arr = [1] # something to add to an array

			if i >= 1:
				# print ret
				# arr.append(1)
				for j in xrange(1, i):
					val = ret[i-1][j-1] + ret[i-1][j]
					arr.append(val)
				arr.append(1)

			ret.append(arr)

		return ret # Should have all rows now