
# Leetcode - https://leetcode.com/problems/rotate-string/


class Solution:
    def rotateString(self, A: str, B: str) -> bool:

        if len(A) != len(B):
            return False

        if A == B:
            return True
        h = {}

        rot = A

        for i in range(0, len(A)):

            print(rot)
            h[rot] = 1
            rot = rot[1:]+rot[0]


        if B in h.keys():
            return True

        return False

# Another solution that is easier
class Solution:
    def rotateString(self, A: str, B: str) -> bool:

        return (A in B+B) and len(A) == len(B)