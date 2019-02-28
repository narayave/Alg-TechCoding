class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0

        count = 0
        prev = nums[0]
        size = len(nums)
        for i in xrange(size):
            print nums, i
            if nums[i] == prev:
                count += 1
                if count > 2:
                    nums = nums[:i] + nums[i+1:]

            else:
                prev = nums[i]
                count = 1

        return len(nums)