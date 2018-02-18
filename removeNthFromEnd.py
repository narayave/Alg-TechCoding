# Leetcode - https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def removeNthFromEnd(self, head, n):
		"""
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""

		if head == None:
			return head

		ret = ListNode(0)
		ret.next = head
		p1 = p2 = ret
		for i in range(n+1):
			p1 = p1.next
		while p1 is not None:
			p1 = p1.next
			p2 = p2.next
		p2.next = p2.next.next
		return ret.next
