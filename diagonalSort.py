
# Leetcode mock interview - https://leetcode.com/problems/sort-the-matrix-diagonally/


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        que = []

        for i in range(0, len(mat)-1):
            que = [(i, 0)] + que
        for i in range(1, len(mat[0])-1):
            que.append((0, i))

        while que:

            item = que.pop()
            i, j = item

            lq = []
            while i < len(mat) and j < len(mat[0]):
                lq.append(mat[i][j])
                i += 1
                j += 1

            print(lq)
            lq = sorted(lq)
            print(lq)

            k, l = item
            while k < len(mat) and l < len(mat[0]):
                mat[k][l] = lq[0]
                lq = lq[1:]
                k += 1
                l += 1

        return mat
