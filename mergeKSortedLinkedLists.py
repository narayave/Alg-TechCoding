
# Leetcode - https://leetcode.com/problems/merge-k-sorted-lists/

import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        print(lists)
        if not lists:
            return

        if len(lists) == 1:
            return lists[0]

        mins = []
        for i, n in enumerate(lists):

            if not n:
                continue
            mins.append((n.val, i))

        heapq.heapify(mins)
        head = ListNode(0)
        tmp = head

        while mins:
            v, i = heapq.heappop(mins)

            tmp.next = lists[i]
            tmp = tmp.next
            if lists[i].next:
                lists[i] = lists[i].next
                heapq.heappush(mins, (lists[i].val, i))


        return head.next