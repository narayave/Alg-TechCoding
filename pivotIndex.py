
# https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1144/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        # Move weights from right to left, until they match

        weight_left, weight_right = 0, sum(nums)

        for i, n in enumerate(nums):

            weight_right -= n

            if weight_right == weight_left:
                return i

            weight_left += n

        return -1

