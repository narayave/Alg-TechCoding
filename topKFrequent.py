
# Leetcode

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        if len(nums) == 1 and k >= 1:
            return nums
        
        count = {}
        
        for i in nums:
            
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
                
        print count
        
        maxFreq = 0
        freq2num = {}
        for key,val in count.items():
            if val in freq2num:
                freq2num[val].append(key)
            else:
                freq2num[val] = [key]
            maxFreq = max(maxFreq,val)
        
        res = []
        for f in range(maxFreq,-1,-1):
            if f in freq2num:
                res += freq2num[f]
            if len(res) >= k:
                return res