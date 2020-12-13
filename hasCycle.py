
# Leetcode - https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode, seen: list = []) -> bool:

        # print(head)

        if not head:
            return False
        curr = head

        while curr.next != None:

            if curr in seen:
                return True

            seen.append(curr)

            curr = curr.next

        return False
