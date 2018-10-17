# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    if l1 == None:
        return l2
    if l2 == None:
        return l1

    l1_save = l1.next
    l2_save = l2.next

    head = None

    if l1.value > l2.value:
        head = l2
    else:
        head = l1

    while l1 != None and l2 != None:

        l1_save = l1.next
        l2_save = l2.next

        if l1.value > l2.value:
            print l1.value, '>', l2.value
            l2.next = l1
            l2 = l2_save
            # l2_save = l2.next
        elif l1.value <= l2.value:
            print l1.value, '<=', l2.value
            l1.next = l2
            l1 = l1_save
            # l1_save = l1.next

        if l1 == None:
            l1.next = l2
            break
        if l2 ==None:
            l2.next = l1
            break

    return head

