

# Leetcode - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        if len(nums) == 1:
            return nums

        output = [nums[0]]

        for i in range(1, len(nums)):
            output.append(output[i-1] + nums[i])

        return output
