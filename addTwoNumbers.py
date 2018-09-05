

# Leetcode - https://leetcode.com/problems/add-two-numbers



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
 
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next



# Saving for later

#         var1 = list()
#         var2 = list()

#         headnode = l1
#         headnode2 = l2
        
#         while headnode != None:
#             var1.append(str(headnode.val))
#             headnode = headnode.next

#         while headnode2 != None:
#             var2.append(str(headnode2.val))
#             headnode2 = headnode2.next
        
#         var1 = var1[::-1]
#         var2 = var2[::-1]
        
#         print var1, var2
        
#         var1 = int(''.join(var1))
#         var2 = int(''.join(var2))
#         res = var1 + var2
#         print var1, var2, res
        
#         res = [int(x) for x in str(res)]
#         print res
               
#         new_node = ListNode(None)
#         for x in xrange(len(res)-1, -1, -1):
#             new_node = ListNode(res[x])
#             print res[x]
        