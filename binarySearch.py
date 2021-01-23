
# https://leetcode.com/explore/learn/card/binary-search/138/background/1038/

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        l = 0
        h = len(nums) - 1

        while l <= h:

            mid = (l+h) // 2

            if nums[mid] == target:
                return mid
            elif nums[l] == target:
                return l
            elif nums[h] == target:
                return h

            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                h = mid - 1
            else:
                break

        return -1