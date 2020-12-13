
# Leetcode - https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        d = {}

        for i in range(0, len(groupSizes)):

            if groupSizes[i] in d.keys():
                d[groupSizes[i]].append(i)
            else:
                d[groupSizes[i]] = [i]

        res = []
        for k in d.keys():
            vallist = d[k]

            this = [vallist[x:x+k] for x in range(0, len(vallist), k)]

            res.extend(this)
        return res
