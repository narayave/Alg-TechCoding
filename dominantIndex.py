
# Leetcode - https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        il, imax = -1, -1
        highestval = -1

        if len(nums) == 1:
            return 0

        for i, n in enumerate(nums):

            if n >= highestval:
                highestval = n
                il = imax
                imax = i
            elif n >= nums[il]:
                il = i

        # print(il, imax)
        if nums[il] * 2 <= nums[imax]:
            return imax
        else:
            return -1

