class Solution(object):
    def combinationSum4(self, nums, target, mem = {}):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        count = 0
        
        if target == 0:
            return 1
        else:
            for i in nums:
                if i <= target:
                    if (i,target-i) not in mem:
                        mem[(i,target-i)] = self.combinationSum4(nums, target-i, mem)
                    count += mem[(i,target-i)]
        print count
        return count
    
