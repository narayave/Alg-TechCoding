
# Leetcode - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        maxcandies = 0

        for i in candies:
            if i > maxcandies:
                maxcandies = i

        res = []

        for i in candies:
            if i+extraCandies >= maxcandies:
                res.append(True)
            else:
                res.append(False)

        return res
