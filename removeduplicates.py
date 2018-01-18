# Facebook Codelab


class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        size = len(A)
        if size < 1:
            return 0
        
        i = 0
        for j in xrange(1, size):
            if A[j] != A[i]:
                i += 1
                A[i] = A[j]
        
        return i + 1
                