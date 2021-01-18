
# Leetcode - https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        h = {}

        for i in range(0, len(nums)):

            val = target - nums[i]

            if val in h:
                return [h[val], i]
            else:
                h[nums[i]] = i
