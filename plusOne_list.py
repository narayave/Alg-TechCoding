
# Leetcode #66

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        
        for i in xrange(0, len(digits)):
            digits[i] = str(digits[i])
        
        digits = int(''.join(digits))
        digits += 1
        digits = [int(x) for x in str(digits)]

        return digits
