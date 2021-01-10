
# Leetcode mock interview - https://leetcode.com/problems/jewels-and-stones/


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        jh = {}

        for j in jewels:
            jh[j] = 0

        for s in stones:

            if s in jh:
                jh[s] += 1

        res = 0
        for i in jh:
            res += jh[i]

        return res
