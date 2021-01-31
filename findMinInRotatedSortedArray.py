
# Leetcode - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:

        if not nums:
            return -1
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        l = 0
        h = n - 1

        while l <= h:
            mid = (l+h) // 2

            if nums[l] == nums[mid] and nums[mid] < nums[h]:
                # This is in a properly sorted array
                return nums[l]
            elif nums[l] == nums[mid] and nums[mid] > nums[h]:
                # This is when l and mid are greater, which means h is the min point
                return nums[h]
            elif nums[l] == nums[h]:
                return nums[h]

            if nums[mid] > nums[h]:
                l = mid+1
            else:
                h = mid
