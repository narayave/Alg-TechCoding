
# Codelab Facebook

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
		
		size = len(A)
		if A < 1:
			return 0
			
		diff = 0
		i = 0
		j = i + 1
		
		# diff = A[j] - A[i]
		# if B > diff:
		#	  return 0

		while i < size - 1 and j < size:
			diff = A[j] - A[i]
			
			if diff == B and i < j:
				return 1
			
			if i == j or diff < B:
				j += 1
			elif diff > B:
				i += 1

		return 0


		# while i < j:
		#	  diff = A[j] - A[i]
		#	  print diff, i, j
		#	  if diff == B:
		#		  return 1
		#	  if i+1 < j:
		#		  d2 = A[j-1] - A[i]			
		#		  d1 = A[j] - A[i+1]

		#		  if d1 >= B and d1 < d2:
		#			  i += 1
		#		  else:
		#			  j -= 1

		#	  else:
		#		  break

		
		# return 0


