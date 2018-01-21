

# Codelab Facebook
# Remove value of duplicates


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):

        # The first way to do would be to take A, go through all the values
        # With a hash map keep track of how many time you see values
        # Then parse through it again and get rid of nodes that have value counts greater than 1

        # If there is only 1 list node, then there are no duplicates, so return
        if A.next == None:
            return A
		
		# O(2n) method 
        # count = {}
        # run = A
        
        # while run != None:
            # if run.val in count:
                # count[run.val] += 1
            # else:
                # count[run.val] = 1

        # #Might need to have a condition separate condition for the first head node
        # head = A
        # print head.value
    
        # while A.next != None:

            # if count[A.next.val] > 1:
                # loop = count[value]
                # tmp = A
                # for i in xrange(loop):
                    # tmp = A.next        
                # A.next = tmp.next
            # else:
                # A = A.next

            # # value = A.val
            # # if count[value] == 1:
            # #     A = A.next
            # # elif count[value] > 1:
            # #     loop = count[value]
            # #     tmp = A
            # #     for i in xrange(loop):
            # #         tmp = A.next        
            # #     A.next = tmp.next
    
    
        # return head



        # I'm thinking of a 2 pointer method where 1 is ahead of the other.
        prev = A  # Pointer 1
        head = A  # This is the head, and we'll update it when we need to.
        
        # Pointer 2
        A = A.next #We are going to start from the 
        
        while A != None:
            
            if prev.val == A.val:
                num = A.val
                while num == prev.val:  # We want to keep traversing till we see another value
                    A = A.next
                    num = A.val
                head = prev
                prev = A
                A = A.next
                
            else:  # Trivial case, when we don't see duplicates
                prev = prev.next
                A = A.next
            
        return head
        
        
	# ACTUAL ANSWER
	def deleteDuplicates(self, A):
        head = result = ListNode('dummy')
        current = A

        while current:
            if current.next and current.val == current.next.val:
                duplicate = current.val
                while current and current.val == duplicate:
                    current = current.next
            else:
                head.next = current
                head = head.next
                current = current.next
        head.next = None
        return result.next
		