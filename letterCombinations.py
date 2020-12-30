
# Leetcode - https://leetcode.com/problems/letter-combinations-of-a-phone-number/


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        h = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        if not digits:
            return []

        res = [""]
        q = []
        for i in digits:
            i_letters = h[int(i)]
            q.append(i_letters)

        # print(q)
        for i in q:
            lans = []
            for k in i:
                for j in res:
                    # print(i,j,k,lans)
                    val = j + k
                    lans.append(val)
            res = lans

        return res
