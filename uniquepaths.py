class Solution:

    # https://leetcode.com/problems/unique-paths/

    def uniquePaths(self, m: int, n: int) -> int:

        y = x = 0
        d = {}
        return self.recurse_func(y, x, d, m, n)

    def recurse_func(self, y, x, d, m, n):

        if (y == m - 1) or (x == n - 1):
            return 1

        if (y, x) in d.keys():
            return d[(y, x)]
        else:
            d[(y, x)] = self.recurse_func(y+1, x, d, m, n) + \
                self.recurse_func(y, x+1, d, m, n)

        return d[(y, x)]
