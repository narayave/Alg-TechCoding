
# Leetcode mock interview - https://leetcode.com/problems/candy/

class Solution:
    def candy(self, ratings: List[int]) -> int:

        if len(ratings) == 1:
            return 1

        res = [1] * len(ratings)

        for i in range(1, len(ratings)):

            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1

        # print(res, ratings)

        for i in range(len(ratings)-2, -1, -1):
            # print(i, res)
            if ratings[i] > ratings[i+1]:
                res[i] = max(res[i], res[i+1]+1)
            # elif ratings[i] == ratings[i+1]:
            #     res[i] = res[i+1]
        # print(res)

        return sum(res)
