
'''
	https://leetcode.com/problems/word-pattern/submissions/

'''

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        str = str.encode('utf-8')
        pattern = pattern.encode('utf-8')
        
        strs = str.split(' ')
        
        if len(pattern) != len(strs):
            return False

        pats = {}
        dict2 = {}
        res = True
        
        for i in xrange(0, len(strs)):
            if strs[i] in pats and pattern[i] in dict2:
                # print i, strs[i], pattern[i]            
                if pats[strs[i]] == pattern[i] and dict2[pattern[i]] == strs[i]:
                    continue
                else:
                    res = False
            else:
                if strs[i] not in pats.keys():
                    pats[strs[i]] = pattern[i]
                else:
                    res = False
                if pattern[i] not in dict2.keys():
                    dict2[pattern[i]] = strs[i]
                else:
                    res = False
                print pats, dict2
        print pats
        print dict2
        
        return res
                
        