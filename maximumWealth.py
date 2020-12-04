
# Leetcode - https://leetcode.com/problems/richest-customer-wealth/


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        maxw = 0
        for acct in accounts:
            csum = sum(acct)

            if csum > maxw:
                maxw = csum

        return maxw
