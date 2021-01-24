
# Leetcode mock interview - https://leetcode.com/problems/construct-k-palindrome-strings/

import math
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        if k > len(s):
            return False
        elif k == len(s):
            return True

        alphs = defaultdict(lambda: 0)

        for i in s:
            alphs[i] += 1


        odds = []
        eventcount = 0

        for j in alphs.keys():
            if alphs[j] % 2 == 1:
                eventcount += 1

        if eventcount > k:
            return False

        return True
