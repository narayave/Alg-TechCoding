
# Leetcode - https://leetcode.com/problems/reverse-words-in-a-string


class Solution:
    def reverseWords(self, s: str) -> str:

        slist = s.split(" ")
        slist = [i for i in slist if i != '']

        slist = slist[::-1]
        print(slist)

        return " ".join(slist)
