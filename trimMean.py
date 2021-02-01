
# Leetcode - https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

class Solution:
    def trimMean(self, arr: List[int]) -> float:

        arr = sorted(arr)

        n = len(arr)

        remove = len(arr)*0.05
        remove = int(remove)
        newarr = arr[remove:-remove]
        sumarr = sum(newarr)
        larr = len(newarr)

        return sumarr/larr
