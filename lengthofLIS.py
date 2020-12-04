
# Leetcode - https://leetcode.com/problems/longest-increasing-subsequence/


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        if len(nums) == 1:
            return 1

        maxn = len(nums)
        arr = [1]*maxn

        for i in range(0, maxn):
            for j in range(0, i):

                if nums[i] > nums[j]:
                    arr[i] = max(arr[i], 1+arr[j])

        return max(arr)
