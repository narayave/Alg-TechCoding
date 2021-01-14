
# Leetcode - https://leetcode.com/problems/goat-latin


class Solution:
    def toGoatLatin(self, S: str) -> str:

        sl = S.split(" ")

        vowels = 'aeiou'

        for i in range(0, len(sl)):

            if sl[i][0].lower() in vowels:
                res = sl[i]+"ma"+("a"*(i+1))
            else:
                res = sl[i][1:]+sl[i][0]+"ma"+("a"*(i+1))
            sl[i] = res

        return " ".join(sl)
