
# Leetcode - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        dummy = ListNode(None, head)

        if not head:
            return
        elif not head.next:
            return head

        p1 = head
        p2 = head.next

        while p2:

            if p1.val == p2.val:
                p1.next = p2.next
                p2 = p2.next
                continue

            p1 = p1.next
            p2 = p2.next

        return dummy.next
