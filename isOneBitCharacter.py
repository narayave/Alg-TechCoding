
# Leetcode mock interview
# https://leetcode.com/problems/1-bit-and-2-bit-characters

# During test - wrote this


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:

        n = len(bits)

        if n == 1:

            if bits[0] == 0:
                return True
            else:
                return False

        # have 2 pointers to always know what you're doing
        i = 0
        j = 1

        while j < n:

            if bits[i] == 0:
                i += 1
                j += 1
            elif bits[i] == 1 and bits[j] == 1:
                i += 2
                j += 2
            elif bits[i] == 1 and bits[j] == 0:

                # Successful answer


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:

        if not bits:
            return False

        n = len(bits)

        i = 0

        while i < n:

            if i == n-1:
                return True

            if bits[i] == 0:
                i += 1
            else:
                i += 2

        return False
