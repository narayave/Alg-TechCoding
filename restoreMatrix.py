
# Leetcode - https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/
# Mock interview with help

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:

        r = len(rowSum)
        c = len(colSum)

        mat = [[0 for i in range(c)] for j in range(r)]
        # print(mat)

        i = 0
        j = 0

        while i < r and j < c:
            mat[i][j] = min(rowSum[i], colSum[j])

            if rowSum[i] == colSum[j]:
                i += 1
                j += 1
            elif rowSum[i] > colSum[j]:
                rowSum[i] -= colSum[j]
                j += 1
            else:
                colSum[j] -= rowSum[i]
                i += 1

        return mat