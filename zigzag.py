class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if len(s) == 1 or numRows == 1:
            return s
        
        inner = []
        for i in xrange(numRows):
            inner.append([])
        print inner

        ind = 0
        flip = 0    # 0 for incrementing order, 1 for decremeting order
        
        for i in xrange(0, len(s)):
            
            inner[ind].append(s[i])
            # print ind, inner
            if flip == 0:
                ind += 1
            elif flip == 1:
#                inner[ind].append(s[i])
                ind -= 1

            if ind == numRows:
                flip = 1
                ind -= 2
            elif ind == 0:
                flip = 0
                
        # print inner
            
        fin = ""
        # Concatenate all lists
        for i in inner:
            i = ''.join(i)
            fin += i
        
        return fin
        
		
		
'''		
Discussion answer:
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)
'''