
# Leetcode - https://leetcode.com/problems/defanging-an-ip-address/submissions/


class Solution:
    def defangIPaddr(self, address: str) -> str:

        res = ""

        for i in address:

            if i == '.':
                res += "[.]"
            else:
                res += str(i)

        return res
