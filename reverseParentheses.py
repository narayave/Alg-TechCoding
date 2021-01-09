
# Leetcode mock interview  - https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/


class Solution:
    def reverseParentheses(self, s: str) -> str:

        stack = []

        i = 0
        while i < len(s):

            if s[i] != ')':
                stack.append(s[i])
                i += 1
                continue

            lr = []
            # stack.append(s[i])
            pop = stack.pop()
            while pop != '(':
                lr.append(pop)
                pop = stack.pop()

            stack.extend(lr)
            i += 1

        return "".join(stack)
