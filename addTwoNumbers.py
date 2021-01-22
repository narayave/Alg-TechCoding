
# Leetcode mock interview - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        val1 = ""
        t = l1
        while t:
            val1 += str(t.val)
            t = t.next
        val2 = ""
        t2 = l2
        while t2:
            val2+= str(t2.val)
            t2 = t2.next

        res = str(eval(val1[::-1]) + eval(val2[::-1]))

        n = 0
        head  = None

        while n < len(res):
            nhead = ListNode(val=int(res[n]), next=head)
            head = nhead
            n += 1

        return nhead