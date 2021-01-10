
# Leetcode mock interview - https://leetcode.com/problems/bulb-switcher/


class Solution:
    def bulbSwitch(self, n: int) -> int:

        #         if n == 0:
        #             return 0

        #         if n == 1:
        #             return 1

        #         b = [0]*n

        #         for i in range(0, n):
        #             for j in range(i, n, i+1):

        #                 if b[j] == 1:
        #                     b[j] = 0
        #                 else:
        #                     b[j] = 1

        #         return sum(b)

        return int(sqrt(n))
