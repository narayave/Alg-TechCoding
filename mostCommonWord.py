
# Leetcode - https://leetcode.com/problems/most-common-word/


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        lowerp = paragraph.lower()

        sp_lp = lowerp.split()

        filtered = [word for word in sp_lp if word not in banned]
        print(filtered)

        d = {}

        for word in filtered:
            if word in d.keys():
                d[word] += 1
            else:
                d[word] = 1

        maxc = 0
        res = None
        for i in d.keys():

            if d[i] >= maxc:
                maxc = d[i]
                res = i

        return res
