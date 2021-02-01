
# Leetcode - https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/
# Mock interview with help

class Solution:
    def minimumDistance(self, word: str) -> int:

        pos = {'A': (0,0), 'B': (0,1), 'C': (0,2), 'D': (0,3), 'E': (0,4), 'F': (0,5),
             'G': (1,0), 'H': (1,1), 'I': (1,2), 'J': (1,3), 'K': (1,4), 'L': (1,5),
             'M': (2,0), 'N': (2,1), 'O': (2,2), 'P': (2,3), 'Q': (2,4), 'R': (2,5),
             'S': (3,0), 'T': (3,1), 'U': (3,2), 'V': (3,3), 'W': (3,4), 'X': (3,5),
             'Y': (4,0), 'Z': (4,1)
            }
        mem = {}

        def cost(letter1: str, letter2: str) -> int:
            if letter1 is None or letter2 is None:
                return 0
            x1, y1 = pos[letter1]
            x2, y2 = pos[letter2]
            return abs(x1 - x2) + abs(y1 - y2)

        def recurse(start, f1, f2):
            if start > len(word)-1:
                return 0
            if (start,f1,f2) in mem:
                return mem[(start,f1,f2)]

            res = min(
                cost(f1, word[start]) + recurse(start + 1, word[start], f2),
                cost(f2, word[start]) + recurse(start + 1, f1, word[start])
            )
            mem[(start,f1,f2)] = res

            return res

        return recurse(0, None, None)
