
# Leetcode mock interview - https://leetcode.com/problems/range-sum-query-2d-immutable/


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        self.mat = matrix
        self.m = len(matrix)
        if matrix:
            self.n = len(matrix[0])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        if row1 < 0 or row2 > self.m:
            return 0
        if col1 < 0 or col2 > self.n:
            return 0

        splmat = self.mat[row1:row2+1]

        nw = []
        for i in splmat:
            nw.extend(i[col1:col2+1])

        calc = 0

        return sum(nw)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
