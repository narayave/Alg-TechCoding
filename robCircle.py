
# Leetcode - https://leetcode.com/problems/house-robber-ii


class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp1, dp2 = 0, 0
        for i in range(0, len(nums)-1):
            tmp = dp1
            dp1 = max(dp2+nums[i], dp1)
            dp2 = tmp
        maxc1 = dp1
        # print(dp1, dp2)

        dp1, dp2 = 0, 0
        for i in range(1, len(nums)):
            tmp = dp1
            dp1 = max(dp2+nums[i], dp1)
            dp2 = tmp
        maxc2 = dp1
        # print(dp1, dp2)

        # print(maxc1, maxc2)
        return max(maxc1, maxc2)
