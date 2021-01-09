
# Leetcode mock interview - https://leetcode.com/problems/can-place-flowers/


class Solution:
    def canPlaceFlowers(self, fb: List[int], n: int) -> bool:

        if n == 0:
            return True

        if n > len(fb):
            return False

        i = 1
        toggle = None
        if fb[0] == 1:
            toggle = True
        else:
            n -= 1
            fb[0] = 1
            toggle = True

        while i < len(fb):

            # print(fb[i], toggle, n, fb)
            if toggle:
                if fb[i] == 0:
                    toggle = False
                else:
                    n += 1
                i += 1
            else:
                if fb[i] == 1:
                    toggle = True
                    i += 1
                elif fb[i] == 0 and n > 0:
                    fb[i] = 1
                    n -= 1
                    i += 1
                    toggle = True
                elif n == 0:
                    break

        if n == 0:
            return True
        else:
            return False
