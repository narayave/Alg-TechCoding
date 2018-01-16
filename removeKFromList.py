# Definition for singly-linked list:
# class ListNode(object):
#	def __init__(self, x):
#	  self.value = x
#	  self.next = None
#
def removeKFromList(l, k):
	
	if l == None:
		return l
	
	track = []
	n = l
	while n != None:
		if n.value == k:	 # If the current value is k, then move header over
			l = n.next
			n = l
			# TODO: There is still one error
			# Test case: [1, 2, 2, 2], k =2
		else:
			print n.value
			# This should be skipping the particular node
			try:
				if n.next.value == k:  # If next value is k, we want to skip
					n.next = n.next.next# Change to next to next-next
			except:
				# n = None
				break
			n = n.next
	return l
	
