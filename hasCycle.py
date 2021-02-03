
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


# O(1) solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        if not head:
            return
        if not head.next:
            return False

        p1 = head
        p2 = head.next

        while p2 and p2.next:
            print(p1.val, p2.val)
            if p1 == p2:
                return True
            p1 = p1.next
            p2 = p2.next.next

        return False
