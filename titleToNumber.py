
# Codelab Facebook

class Solution:
	# @param A : string
	# @return an integer
	def titleToNumber(self, A):
		# Should use memoization for maximum effectiveness.
		alphabets = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
		# list(alphabets)
		run = list(A.upper())	# Sanitize input
		# print run

		memo = {}
		for i in xrange(1, len(alphabets)+1):
			memo[alphabets[i-1]] = i
		# print memo

		count = 0
		run = run[::-1]

		for i in xrange(0, len(run)):

			count += (26 ** (i)) * memo[run[i]]


			# if i == (len(run) - 1):
			#	  count += memo[run[i]]
			# else:
			#	  add = len(alphabets) * (i * memo[run[i]])
			#	  print add
			#	  count += add # len(alphabets) * (i+1)

			# print i, count, run[i]

		# for i in xrange(len(run)-1, -1, -1):
		#	  count += memo[run[i]]
		#	  if i > 0:
		#		  count += len(alphabets) * (i+1)
		#	  # count += (len(alphabets) * i) - memo[run[i-1]]
		#	  print i, count

		return count

