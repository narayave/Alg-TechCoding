
# Leetcode - https://leetcode.com/explore/learn/card/binary-search/126/template-ii/947/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        l = 1
        h = n

        while l <= h:
            mid = (l+h) // 2
            print(l, mid, h)
            if isBadVersion(mid) == True:
                h = mid - 1
            else:
                l = mid + 1

        return l
