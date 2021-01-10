
# Leetcode ock interview - https://leetcode.com/problems/subsets/


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return [[]]

        if len(nums) == 1:
            return [[], [nums[0]]]

        res = [[]]

        count = 0
        for i in nums[count:]:
            lq = []
            for j in res:
                lq.append(j+[i])
            res.extend(lq)
            count += 1

        return res
