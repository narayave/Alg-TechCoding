
# Leetcode mock interview - https://leetcode.com/problems/car-pooling/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        minkm = min([i[1] for i in trips])
        maxkm = max([i[2] for i in trips])
        print(minkm, maxkm)

        print(trips)
        cap = capacity

        for i in range(minkm, maxkm+1):

            local_cap = []
            for t in trips:
                pers, start, dest = t[0], t[1], t[2]

                if start < i and i < dest:
                    continue

                if i == start:
                    local_cap.append(-pers)
                if i == dest:
                    local_cap.append(pers)

            cap += sum(local_cap)
            if cap < 0 or cap > capacity:
                return False

        return True
