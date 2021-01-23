
# https://leetcode.com/explore/learn/card/binary-search/125/template-i/952/

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binsearch(nums, target, l, h):

            if l > h:
                return -1

            mid = (l+h) // 2

            print(nums[l], nums[mid], nums[h])

            if nums[mid] == target:
                print('1')
                return mid
            elif nums[l] <= nums[mid]:
                print('2')
                if target >= nums[l] and target <= nums[mid]:
                    return binsearch(nums, target, l, mid-1)
                else:
                    return binsearch(nums, target, mid+1, h)
            else:
                print('3')
                if target >= nums[mid] and target <= nums[h]:
                    return binsearch(nums, target, mid+1, h)
                else:
                    return binsearch(nums, target, l, mid-1)

        l = 0
        h = len(nums) - 1
        return binsearch(nums, target, l, h)
