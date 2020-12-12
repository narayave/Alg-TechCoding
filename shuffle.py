
# Leetcode - https://leetcode.com/problems/shuffle-the-array/


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        # mid = len(nums) // 2
        firsthalf = nums[:n]
        sechalf = nums[n:]

        res = []

        for i in range(0, n):

            res.append(firsthalf[i])
            res.append(sechalf[i])

        return res
