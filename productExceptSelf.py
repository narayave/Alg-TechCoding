
# Leetcode - https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        out = [1] * n

        for i in range(1, len(nums)):
            out[i] = nums[i-1] * out[i-1]


        rightp = 1
        for i in range(n-1, -1, -1):
            out[i] *= rightp
            rightp *= nums[i]

        return out