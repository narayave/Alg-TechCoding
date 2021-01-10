
# Leetocde mock interview - https://leetcode.com/problems/buddy-strings/


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:

        if len(A) != len(B):
            return False

        adiff = []
        bdiff = []
        ah = defaultdict(lambda: 0)

        n = len(A)

        for i in range(0, len(A)):

            ah[A[i]] += 1
            if A[i] == B[i]:
                continue

            adiff.append(A[i])
            bdiff.append(B[i])

        if len(adiff) > 0:
            if len(adiff) > 2:
                return False
            if set(adiff).issubset(set(bdiff)):
                return True
            else:
                return False

        for i in ah:
            print(ah[i])
            if (ah[i] % 2 == 0) or ((ah[i] > 2)):
                return True

        return False
