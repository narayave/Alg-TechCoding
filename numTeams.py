
# Leetcode - https://leetcode.com/problems/count-number-of-teams/


# The following solution almost works, but doesn't pass all test cases
class Solution:
    def numTeams(self, ratings: List[int]) -> int:

        if not ratings or len(ratings) < 3:
            return 0

        i, j, k = 0, 1, 2
        h = defaultdict(lambda: 0)

        def check(i, j, k) -> int:

            i, j, k = ratings[i], ratings[j], ratings[k]
            if (i < j and j < k) or (i > j and j > k):
                return 1

            return 0

        res = 0
        n = len(ratings)

        q = [(i,j,k)]
        while q:

            i,j,k  = q.pop(0)

            # print(ratings[i],ratings[j],ratings[k])
            res += check(i,j,k)

            if k < n-1:
                if (i,j,k+1) not in h:
                    q.append((i,j,k+1))
                    h[(i,j,k+1)] = 1
            if j < n-2 and k < n-1:
                if (i,j+1,k+1) not in h:
                    q.append((i,j+1,k+1))
                    h[(i,j+1,k+1)] = 1
            if i < n-3 and j < n-2 and k < n-1:
                if (i+1,j+1,k+1) not in h:
                    q.append((i+1,j+1,k+1))
                    h[(i+1,j+1,k+1)] = 1

        return res



# This solution apparently is better
from collections import defaultdict

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3:
            return 0

        greater = defaultdict(int)
        less = defaultdict(int)
        res = 0

		# greater[i] is the number of elements after index i greater than ratings[i]
        for i in range(len(rating)-1):
            for j in range(i+1, len(rating)):
                if rating[j] > rating[i]:
                    greater[i] += 1
                else:
                    less[i] += 1

		# Accumulate counts
        for i in range(len(rating)-2):
            for j in range(i+1, len(rating)):
                if rating[i] < rating[j]:
                    res += greater[j]
                else:
                    res += less[j]

        return res