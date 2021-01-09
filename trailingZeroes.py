
# Leetcode - https://leetcode.com/problems/factorial-trailing-zeroes/


class Solution:
    def trailingZeroes(self, n: int) -> int:

        if n == 0:
            return 0

        res = 1
        cnt = 0

        while n > 1:

            res *= n
            n -= 1

        res_str = str(res)
        j = len(res_str) - 1
        while j >= 0:
            # print(j, res_str[j], res_str, cnt)
            if res_str[j] == '0':
                cnt += 1
                j -= 1
            else:
                return cnt
