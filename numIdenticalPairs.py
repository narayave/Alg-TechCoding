
# Leetcode - https://leetcode.com/problems/number-of-good-pairs/


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        d = {}
        res = 0

        for i in nums:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 0

        for i in d.keys():
            val = d[i]

            # infinite series equation = n(n+1)/2
            fin = (val*(val+1)) // 2
            res += int(fin)

        return res
