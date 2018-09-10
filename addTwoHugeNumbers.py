# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def addTwoHugeNumbers(a, b):
    num1 = ''
    num2 = ''

    while a != None:
        val = str(a.value)
        while len(val) != 4:
            val = '0'+val

        num1 += val
        a = a.next

    while b != None:
        val = str(b.value)
        while len(val) != 4:
            val = '0'+val

        num2 += val
        b = b.next

    print num1, num2

    res = int(num1) + int(num2)
    print res

    res = str(res)
    pointer = None
    while len(res) != 0:
        val = res[-4:]
        res = res[:-4]
        print int(val)
        item = ListNode(int(val))
        item.next = pointer
        pointer = item

    return item