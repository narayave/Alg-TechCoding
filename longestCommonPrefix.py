
'''
	https://leetcode.com/problems/longest-common-prefix/
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        
        i = 0   # Go through characters in a word
        j = 0   # Go through list of strings
        output = ''
        if len(strs[0]) != 0:
            ref = strs[0][i]
        else:
            return output
            
        
        while i <= len(strs[0]):
            for j in strs:
                if i < len(j):
                    if ref != j[i]:
                        return output
                else:
                    return output
            output = str(output) + str(ref)
            i += 1
            if i < len(strs[0]):
                ref = strs[0][i]
            else:
                break
        return output
