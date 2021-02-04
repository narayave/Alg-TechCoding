
# Leetcode mock interview - https://leetcode.com/problems/restore-ip-addresses/
# Not my solution

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        n = len(s)

        if n < 4:
            return []
        elif n == 4:
            return [f"{s[0]}.{s[1]}.{s[2]}.{s[3]}"]
        elif n > 12:
            return []

        res = []

        def validate(i, coll):
            # print(i, coll, res)
            if len(coll) > 4 or i > len(s): return
            if len(coll) == 4 and i == len(s):
                res.append(".".join(coll))
            for j in range(1,4):
                c = s[i : i+j]
                # print(c)
                if len(c) > 1 and c[0] == '0': continue
                if c and 0 <= int(c) <= 255:
                    validate(i+j, coll + [c])


        validate(0, [])
        return res