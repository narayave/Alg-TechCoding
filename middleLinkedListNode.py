
# Leetcode - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, h: ListNode) -> ListNode:

        head = h
        head2 = h

        while head2 and head2.next:

            print(head.val, head2.val)

            head2 = head2.next.next
            head = head.next

        return head
