
# Leetcode mock interview - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        tmphead = head
        fk_node = ListNode(0, head)
        nodelist = [fk_node]

        while tmphead:
            nodelist.append(tmphead)
            tmphead = tmphead.next

        if len(nodelist) == 1 and n == 1:
            return

        item1 = nodelist[-n]
        if n == 1:
            item1 = nodelist[-2]
            item1.next = None
        if n >= 2:
            item1 = nodelist[-n-1]
            item1.next = item1.next.next

        return nodelist[0].next
