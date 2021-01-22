
# Leetcode mock interview - https://leetcode.com/problems/roman-to-integer/


class Solution:
    def romanToInt(self, s: str) -> int:

        rh = {'I': 1, 'V': 5, 'X': 10,
              'L': 50, 'C': 100, 'D': 500,
              'M': 1000, 'IV': 4, 'IX': 9,
              'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

        if len(s) == 1:
            return rh[s]

        i = 0
        j = 2
        res = 0

        while j <= len(s)+1:
            item = s[i:j]
            # print(item)
            if item in rh:
                res += rh[item]
                j += 2
                i += 2
            else:
                res += rh[s[i]]
                j += 1
                i += 1

        return res