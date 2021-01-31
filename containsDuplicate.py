
# Leetcode - https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        h = defaultdict(lambda: 0)

        for i in nums:

            if h[i] == 0:
                h[i] += 1
            else:
                return True

        return False
