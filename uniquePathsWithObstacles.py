
# Leetcode - https://leetcode.com/problems/unique-paths-ii/


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):

            if obstacleGrid[i][0] != 1:
                dp[i][0] = 1
            else:
                break

        for j in range(n):
            if obstacleGrid[0][j] != 1:
                dp[0][j] = 1
            else:
                break

        for k in range(1, m):
            for l in range(1, n):
                if obstacleGrid[k][l] == 1:
                    dp[k][l] = 0
                else:
                    dp[k][l] = dp[k-1][l] + dp[k][l-1]

        return dp[-1][-1]
