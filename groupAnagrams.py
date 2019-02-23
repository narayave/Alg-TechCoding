
'''
	https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1124/
'''


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        dicts = {}
        
        for i in strs:
            s_i = ''.join(sorted(i))
            if s_i in dicts.keys():
                dicts[s_i].append(i)
            else:
                dicts[s_i] = [i]
                
        return dicts.values()