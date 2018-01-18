
# Codelab Facebook

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        
        if A == []:
            return 1
        
        num_s = str(''.join([str(x) for x in A]))
        size = len(num_s)
        # print size
        
        num_i = int(num_s) + 1
        # print num_i
        
        num = list(str(num_i))
        # print num
        num = [int(x) for x in num]
        
        return num