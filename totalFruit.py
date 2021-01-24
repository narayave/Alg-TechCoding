
# Leetcode mock interview - https://leetcode.com/problems/fruit-into-baskets/

# Need to more thoroughly solve this

class Solution:
    def totalFruit(self, tree: List[int]) -> int:

        prev, curr, res = [None, 0], [None, 0], 0
        for t in tree:

            print(t, prev, curr, res)

            if t == curr[0]:
                curr[1] += 1
            else:
                prev, curr = curr, prev
                if t == curr[0]:
                    prev[1] += curr[1]
                else:
                    res = max(res, prev[1] + curr[1])
                curr = [t, 1]
        return max(res, prev[1]+curr[1])
