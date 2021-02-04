
# Leetcode - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        loc = ""
        st = 0
        i = 0
        if not s:
            return 0
        curmax = 0
        maxval = 0
        while i < len(s):
            if s[i] not in loc:
                loc += s[i]
                curmax += 1
                if curmax > maxval: maxval = curmax
            else:
                ind = loc.find(s[i])
                # print(ind, loc)
                loc = loc[ind+1:i] + s[i]
                curmax = len(loc)
            i += 1
        return maxval