
# Leetcode - https://leetcode.com/problems/majority-element/

import math

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n = len(nums)

        limit = math.floor(n/3)

        # print(limit)

        h = defaultdict(lambda: 0)

        for i in nums:
            h[i] += 1

        res = []

        for j in h.keys():
            # print(h[j], limit)
            if h[j] > limit:
                res.append(j)

        return res