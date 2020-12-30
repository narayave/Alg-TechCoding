
# Leetcode - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = ListNode()
        runner = head

        while l1 and l2:
            # print(l1.val, l2.val)
            if l1.val <= l2.val:
                runner.next = l1
                l1 = l1.next
            elif l1.val > l2.val:
                runner.next = l2
                l2 = l2.next
            runner = runner.next
            # print(runner.val)
        runner.next = l1 or l2

        return head.next
