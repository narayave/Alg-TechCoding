

'''
	Leetcode - https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None or head.next == None:
            return head
        
        
        p1 = head
        p2 = head.next
        p3 = head.next
        
        p1.next = None
        
        while p3.next != None:
            #print p1.val, p2.val, p3.val
            p3 = p3.next
            p2.next = p1
            p1 = p2
            p2 = p3
            #print p1.val, p2.val, p3.val
    
        p2.next = p1
        return p2
        